# tools/__init__.py
from .weather import get_weather
from .dealership import get_dealership_address
from .appointment import check_appointment_availability, schedule_appointment


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather information for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The name of the city to get weather for"
                    }
                },
                "required": ["city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_dealership_address",
            "description": "Get the address of a SuperCar dealership",
            "parameters": {
                "type": "object",
                "properties": {
                    "dealership_id": {
                        "type": "string",
                        "description": "The ID of the dealership (e.g., 'nyc', 'la', 'chicago')"
                    }
                },
                "required": ["dealership_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "check_appointment_availability",
            "description": "Check available appointment slots for a test drive",
            "parameters": {
                "type": "object",
                "properties": {
                    "dealership_id": {
                        "type": "string",
                        "description": "The ID of the dealership"
                    },
                    "date": {
                        "type": "string",
                        "description": "The date for the appointment (YYYY-MM-DD)"
                    }
                },
                "required": ["dealership_id", "date"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "schedule_appointment",
            "description": "Schedule an appointment for a test drive",
            "parameters": {
                "type": "object",
                "properties": {
                    "dealership_id": {
                        "type": "string",
                        "description": "The ID of the dealership"
                    },
                    "date": {
                        "type": "string",
                        "description": "The date for the appointment (YYYY-MM-DD)"
                    },
                    "time": {
                        "type": "string",
                        "description": "The time for the appointment (HH:MM)"
                    },
                    "car_model": {
                        "type": "string",
                        "description": "The car model for the test drive"
                    },
                    "user_id": {
                        "type": "string",
                        "description": "ID of the user booking the appointment"
                    }
                },
                "required": ["dealership_id", "date", "time", "car_model", "user_id"]
            }
        }
    }
]

async def process_tool_call(function_name: str, arguments: dict):
    """Process a tool call and return the result"""
    try:
        if function_name == "get_weather":
            return get_weather(**arguments)
        elif function_name == "get_dealership_address":
            return get_dealership_address(**arguments)
        elif function_name == "check_appointment_availability":
            return check_appointment_availability(**arguments)
        elif function_name == "schedule_appointment":
            return schedule_appointment(**arguments)
        else:
            return {"error": f"Unknown function: {function_name}"}
    except Exception as e:
        return {"error": str(e)} 