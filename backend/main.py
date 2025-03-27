import os
import json
from typing import Dict, List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
from dotenv import load_dotenv

from models import QueryRequest
from tools import tools
from utils.stream import create_stream_generator
from llm import generate_completion

load_dotenv()

app = FastAPI(title="SuperCar Virtual Sales Assistant API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store conversation history by session ID
conversation_history: Dict[str, List[Dict[str, str]]] = {}

@app.get("/")
async def root():
    return {"message": "SuperCar Virtual Sales Assistant API is running"}

@app.post("/query")
async def query(request: QueryRequest):
    session_id = request.session_id
    user_query = request.query
    
    if session_id not in conversation_history:
        conversation_history[session_id] = [
            {
                "role": "system", 
                "content": """You are Lex, a virtual sales assistant for SuperCar dealerships. 
                Help customers with information about cars, schedule test drives, and provide dealership information.
                Always be friendly, knowledgeable, and helpful. If you don't know something, use the appropriate tool to find the information."""
            }
        ]
    
    conversation_history[session_id].append({"role": "user", "content": user_query})
    
    completion_stream = generate_completion(
        messages=conversation_history[session_id].copy(),
        tools=tools
    )
    
    generator = create_stream_generator(
        completion_stream=completion_stream, 
        session_id=session_id,
        messages=conversation_history[session_id]
    )
    
    return EventSourceResponse(generator)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)