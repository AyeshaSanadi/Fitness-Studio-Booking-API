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


## Setup Instructions (Windows CMD)

### 1. Clone the Repository

> If you have **Git for Windows** installed (e.g., via Git Bash or Git CMD), you can use:

```cmd
git clone https://github.com/AyeshaSanadi/Fitness-Studio-Booking-API.git
cd Fitness-Studio-Booking-API
```

> If you **don’t have Git**, download the project as a ZIP file from GitHub and extract it manually.



### 2. Create a Virtual Environment

```cmd
python -m venv venv
```

### 3. Activate the Virtual Environment

```cmd
venv\Scripts\activate
```


### 4. Install Dependencies

```cmd
pip install fastapi uvicorn pydantic[email]
```

> If you're using `EmailStr` in your FastAPI models, make sure to install with `[email]` extras for email validation.



### 5. Run the API Server

```cmd
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
