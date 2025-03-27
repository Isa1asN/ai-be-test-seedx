import json
import asyncio
from typing import Dict, Any, List, AsyncGenerator
from sse_starlette.sse import EventSourceResponse
from tools.weather import get_weather
from tools.dealership import get_dealership_address
from tools.appointment import check_appointment_availability, schedule_appointment
from llm import get_groq_client
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

async def create_stream_generator(completion_stream, session_id: str, messages: List[Dict[str, str]]) -> AsyncGenerator[Dict[str, Any], None]:
    """Generate streaming events for SSE response"""
    try:
        buffer = ""
        tool_name = None
        tool_args = ""
        tool_call_id = None
        
        for chunk in completion_stream:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                buffer += content
                yield {"event": "chunk", "data": content}
            
            if chunk.choices[0].delta.tool_calls:
                tool_call = chunk.choices[0].delta.tool_calls[0]
                
                if tool_call.id:
                    tool_call_id = tool_call.id
                
                if tool_call.function and tool_call.function.name:
                    tool_name = tool_call.function.name
                    yield {"event": "tool_use", "data": tool_name}
                
                if tool_call.function and tool_call.function.arguments:
                    tool_args += tool_call.function.arguments
                
                if tool_args and tool_args.strip().endswith("}"):
                    try:
                        args = json.loads(tool_args)
                        result = None
                        
                        if tool_name == "get_weather":
                            result = get_weather(**args)
                        elif tool_name == "get_dealership_address":
                            result = get_dealership_address(**args)
                        elif tool_name == "check_appointment_availability":
                            result = check_appointment_availability(**args)
                        elif tool_name == "schedule_appointment":
                            result = schedule_appointment(**args)
                        
                        if result:
                            logger.debug(f"Tool output: {json.dumps(result, indent=2)}")
                            
                            tool_output = result
                            yield {"event": "tool_output", "data": json.dumps(tool_output)}
                            
                            messages.append({
                                "role": "tool",
                                "tool_call_id": tool_call_id,
                                "name": tool_name,
                                "content": json.dumps(result)
                            })
                            
                            final_response = get_groq_client().chat.completions.create(
                                model="llama-3.3-70b-versatile",
                                messages=messages,
                                stream=True
                            )
                            
                            async for final_chunk in wrap_stream(final_response):
                                if final_chunk.choices[0].delta.content:
                                    content = final_chunk.choices[0].delta.content
                                    yield {"event": "chunk", "data": content}
                    
                    except Exception as e:
                        print(f"Error executing tool: {str(e)}")
                        yield {"event": "error", "data": str(e)}
        
        yield {"event": "end", "data": ""}
        
    except Exception as e:
        print(f"Error in stream_generator: {str(e)}")
        yield {"event": "error", "data": str(e)}
        yield {"event": "end", "data": ""}

async def wrap_stream(stream):
    """Wrap a synchronous iterator to make it an async iterator"""
    for chunk in stream:
        yield chunk
        await asyncio.sleep(0)

async def process_tool_call(function_name: str, arguments: dict):
    """Process a tool call and return the result"""
    try:
        if function_name == "get_weather":
            from tools.weather import get_weather
            return get_weather(**arguments)
        elif function_name == "get_dealership_address":
            from tools.dealership import get_dealership_address
            return get_dealership_address(**arguments)
        elif function_name == "check_appointment_availability":
            from tools.appointment import check_appointment_availability
            return check_appointment_availability(**arguments)
        elif function_name == "schedule_appointment":
            from tools.appointment import schedule_appointment
            return schedule_appointment(**arguments)
        else:
            return {"error": f"Unknown function: {function_name}"}
    except Exception as e:
        return {"error": str(e)}