# Fitness Studio Booking API 🏋️‍♀️ 

This is a simple FastAPI project that allows clients to:

- View available fitness classes
- Book a class
- View bookings by email


## Features

- List all upcoming fitness classes
- Filter classes by scheduled time and timezone
- Book a spot in a fitness class
- Retrieve all bookings by email


## Dependencies

* FastAPI
* Pydantic
* zoneinfo (standard in Python 3.9+)


## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/AyeshaSanadi/Fitness-Studio-Booking-API.git
cd fitness-booking-api
````

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn pydantic
```

### 4. Run the API

```bash
uvicorn main:app --reload
```

## Notes

* Timezone support is handled using `zoneinfo` (Python 3.9+ required).
* Booking slots decrease after each successful booking.
* Use tools like [Postman](https://www.postman.com/) or [httpie](https://httpie.io/) for easier testing.


## API Endpoints & Sample Usage (Windows CMD)

### 1. Get All Classes

**Endpoint**: `GET /classes`

**Optional Query Params**:

* `scheduled_time` (ISO format): `2025-06-18T07:00:00`
* `target_timezone`: `America/New_York`, `Asia/Kolkata`, etc.

**Windows CMD cURL**:

```cmd
curl -X GET "http://localhost:8000/classes?target_timezone=Asia/Kolkata" -H "accept: application/json"
```

---

### 2. Book a Class

**Endpoint**: `POST /book`

**Request Body**:

```json
{
  "id": 2,
  "class_id": 1,
  "client_name": "John Doe",
  "client_email": "john@example.com"
}
```

**Windows CMD cURL** (Note the escaped quotes):

```cmd
curl -X POST "http://localhost:8000/book" -H "Content-Type: application/json" -d "{\"id\":2,\"class_id\":1,\"client_name\":\"John Doe\",\"client_email\":\"john@example.com\"}"
```

### 3. Get Bookings by Email

**Endpoint**: `GET /bookings/{email_id}`

**Example for `john@example.com`**:

```cmd
curl -X GET "http://localhost:8000/bookings/john@example.com"
```

## API Exploration with Swagger
FastAPI provides an automatic interactive API documentation (Swagger UI):

After starting the server, go to: http://localhost:8000/docs

You can use it to try all endpoints in your browser with sample inputs.

![image](https://github.com/user-attachments/assets/7ec1c1ca-67f4-4581-9cc2-31608f680890)
 --
