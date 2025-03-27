def get_dealership_address(dealership_id: str) -> dict:
    """Mock dealership data for demonstration purposes"""
    dealerships = {
        "nyc": {
            "name": "SuperCar New York City",
            "address": "123 Broadway, New York, NY 10001",
            "phone": "+1 (212) 555-1234",
            "hours": "Mon-Sat: 9:00 AM - 8:00 PM",
            "email": "nyc@supercar.com"
        },
        "la": {
            "name": "SuperCar Los Angeles",
            "address": "456 Hollywood Blvd, Los Angeles, CA 90028",
            "phone": "+1 (310) 555-5678",
            "hours": "Mon-Sat: 9:00 AM - 8:00 PM",
            "email": "la@supercar.com"
        },
        "chicago": {
            "name": "SuperCar Chicago",
            "address": "789 Michigan Ave, Chicago, IL 60611",
            "phone": "+1 (312) 555-9012",
            "hours": "Mon-Sat: 9:00 AM - 8:00 PM",
            "email": "chicago@supercar.com"
        }
    }
    
    dealership = dealerships.get(dealership_id.lower(), {
        "name": f"SuperCar {dealership_id}",
        "address": "Information not available",
        "phone": "Information not available",
        "hours": "Mon-Sat: Hours not available",
        "email": "Information not available"
    })

    return {
        "name": "get_dealership_address",
        "output": (
            f"The {dealership['name']} dealership is located at {dealership['address']}. "
            f"Contact: {dealership['phone']}. Hours: {dealership['hours']}. "
            f"Email: {dealership['email']}"
        )
    }