import os
import groq
import json
from dotenv import load_dotenv
from typing import List, Dict, Any

load_dotenv()

def get_groq_client():
    """Initialize and return the Groq client"""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is not set")
    
    return groq.Client(api_key=api_key)

def generate_completion(messages: List[Dict[str, str]], tools: List[Dict[str, Any]]):
    """Generate a streaming completion from Groq LLM"""
    client = get_groq_client()
    
    messages.append({
        "role": "system",
        "content": """When you need information, follow these steps:
1. Think about what tool you need
2. Call the tool with appropriate parameters
3. Use the tool's response to provide a helpful answer
Format: Always use complete sentences."""
    })
    
    return client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=messages,
        tools=tools,
        stream=True,
        tool_choice="auto",
        max_tokens=2048
    )