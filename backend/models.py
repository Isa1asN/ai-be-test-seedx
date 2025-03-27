from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Union

class QueryRequest(BaseModel):
    query: str
    session_id: str

class WeatherInput(BaseModel):
    city: str

class DealershipInput(BaseModel):
    dealership_id: str

class AppointmentAvailabilityInput(BaseModel):
    dealership_id: str
    date: str  # YYYY-MM-DD format

class ScheduleAppointmentInput(BaseModel):
    user_id: str
    dealership_id: str
    date: str  # YYYY-MM-DD format
    time: str  # HH:MM format
    car_model: str

class ToolUseEvent(BaseModel):
    name: str
    input: Dict[str, Any]

class ToolOutputEvent(BaseModel):
    name: str
    output: Dict[str, Any]

class ToolOutput(BaseModel):
    name: str
    output: Dict[str, Any]

class Message(BaseModel):
    role: str
    content: str 