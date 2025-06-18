from pydantic import BaseModel, EmailStr
from datetime import datetime

# Model representing a fitness class
class FitnessClass(BaseModel):
    id: int
    name: str
    scheduled_time: datetime
    instructor: str
    available_slot: int

# Model representing a booking
class Booking(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr
