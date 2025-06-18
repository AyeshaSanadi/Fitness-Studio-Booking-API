from model import FitnessClass, Booking
from datetime import datetime
from zoneinfo import ZoneInfo

# Set the default timezone to Asia/Kolkata
IST = ZoneInfo("Asia/Kolkata")

# In-memory storage for class details
class_details = {
    1: FitnessClass(
        id=1,
        name="Yoga",
        scheduled_time=datetime(2025, 6, 18, 7, 0, tzinfo=IST),
        instructor="Alice",
        available_slot=10
    ),
    2: FitnessClass(
        id=2,
        name="Zumba",
        scheduled_time=datetime(2025, 6, 18, 9, 0, tzinfo=IST),
        instructor="Bob",
        available_slot=5
    )
}

# In-memory storage for booking details, keyed by client email
booking_details = {
    "test@example.com": [
        Booking(id=1, class_id=1, client_name="Test User", client_email="test@example.com")
    ]
}
