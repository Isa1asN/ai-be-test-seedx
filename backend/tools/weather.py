import random

def get_weather(city: str) -> dict:
    """Mock weather data for demonstration purposes"""
    conditions = ["Sunny", "Cloudy", "Rainy", "Partly Cloudy", "Clear"]
    temp = random.randint(15, 35)
    humidity = random.randint(30, 90)
    wind_speed = random.randint(0, 30)
    
    return {
        "name": "get_weather",
        "output": f"Weather in {city}: Temperature: {temp}°C, Condition: {random.choice(conditions)}, Humidity: {humidity}%, Wind Speed: {wind_speed}km/h"
    }