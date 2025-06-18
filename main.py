from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
from typing import Optional
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from model import Booking
from data import class_details, booking_details

app = FastAPI()

# Endpoint to get all upcoming classes, optionally filtered by scheduled_time and timezone
@app.get("/classes")
async def get_all_upcoming_classes(
    scheduled_time: Optional[datetime] = Query(None),
    target_timezone: Optional[str] = Query("Asia/Kolkata")
    ):
    try:
        # Try to get the requested timezone
        tz = ZoneInfo(target_timezone)
    except ZoneInfoNotFoundError:
        # Return error if timezone is invalid
        raise HTTPException(status_code=400, detail="Invalid timezone")

    results = []
    for class_obj in class_details.values():
        # Convert class time to the requested timezone
        class_time_in_target = class_obj.scheduled_time.astimezone(tz)
        # If no scheduled_time filter or times match, add to results
        if scheduled_time is None or class_obj.scheduled_time.astimezone(tz).replace(microsecond=0) == scheduled_time.replace(microsecond=0):
            # Copy the class object and update the scheduled_time to the requested timezone
            updated_class = class_obj.model_copy()
            updated_class.scheduled_time = class_time_in_target
            results.append(updated_class)
    
    if results:
        return results
    # If no classes found, return 404
    raise HTTPException(status_code=404, detail="No matching classes found.")

# Endpoint to book a client into a class
@app.post("/book")
async def book_client(request: Booking):
    # Get the class object by ID
    class_obj = class_details.get(request.class_id)
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")

    # Check if there are available slots
    if class_obj.available_slot <= 0:
        raise HTTPException(status_code=400, detail="No available slots")

    # Decrement available slots
    class_obj.available_slot -= 1

    # Create a new booking
    new_booking = Booking(
        id=len(booking_details.get(request.client_email, [])) + 1,
        class_id=request.class_id,
        client_name=request.client_name,
        client_email=request.client_email
    )

    # Add the booking to the booking details
    booking_details.setdefault(request.client_email, []).append(new_booking)

    return {
        "message": "Booking successful",
        "booking": new_booking
    }

# Endpoint to get all bookings for a given email
@app.get("/bookings/{email_id}")
async def get_bookings(email_id: str):
    detail = booking_details.get(email_id)
    if detail:
        return detail
    # If no bookings found, return 404
    raise HTTPException(status_code=404, detail="No bookings found for the provided email.")
