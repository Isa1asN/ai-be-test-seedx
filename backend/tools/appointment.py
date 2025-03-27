import random
from datetime import datetime, timedelta

def check_appointment_availability(dealership_id: str, date: str) -> dict:
    """Mock appointment availability data for demonstration purposes"""
    dealerships = {
        "nyc": "SuperCar New York City",
        "la": "SuperCar Los Angeles",
        "chicago": "SuperCar Chicago"
    }
    dealership_name = dealerships.get(dealership_id.lower(), f"SuperCar {dealership_id}")
    
    available_slots = []
    hour = 9
    while hour < 17:
        if random.random() > 0.3:  # 70% chance slot is available
            available_slots.append(f"{hour:02d}:00")
        if random.random() > 0.3:
            available_slots.append(f"{hour:02d}:30")
        hour += 1
    
    slots_text = ", ".join(available_slots)
    
    return {
        "name": "check_appointment_availability",
        "output": f"Available appointment slots at {dealership_name} on {date}: {slots_text}"
    }

def schedule_appointment(dealership_id: str, date: str, time: str, car_model: str, user_id: str) -> dict:
    """Mock appointment scheduling for demonstration purposes"""
    dealerships = {
        "nyc": "SuperCar New York City",
        "la": "SuperCar Los Angeles",
        "chicago": "SuperCar Chicago"
    }
    dealership_name = dealerships.get(dealership_id.lower(), f"SuperCar {dealership_id}")
    confirmation_id = f"SC-{random.randint(10000, 99999)}"
    
    return {
        "name": "schedule_appointment",
        "output": (
            f"Appointment confirmed! Your test drive for the {car_model} is scheduled at "
            f"{dealership_name} on {date} at {time}. Confirmation ID: {confirmation_id}. "
            f"Please arrive 15 minutes before your appointment and bring a valid driver's license."
        )
    }

def get_dealership_name(dealership_id: str) -> str:
    """Helper function to get dealership name from ID"""
    dealerships = {
        "nyc": "SuperCar New York City",
        "la": "SuperCar Los Angeles",
        "chicago": "SuperCar Chicago"
    }
    return dealerships.get(dealership_id.lower(), f"SuperCar {dealership_id}")