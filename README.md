# ✈️ Flight Search API (FastAPI + MySQL)

This project is a **simple Flight Search API** built using **FastAPI** and **MySQL**. It allows you to add, view, search, and delete flight information. The project is designed for **beginners** and demonstrates the use of FastAPI with a MySQL backend.

---

## 🧾 Features

- Add new flights ✈️
- List all flights 📄
- Search flights by source, destination, and date 🔍
- Get flight by ID 🆔
- Delete a flight ❌

---

## 📁 Project Structure

flight_search/
│
├── main.py # Entry point of the app
├── controller.py # API endpoints (routes)
├── database.py # DB connection config
├── models.py # SQLAlchemy models (tables)
├── schemas.py # Pydantic models for request/response
├── services.py # Business logic (CRUD)
└── README.md # This file



---

## 🧑‍💻 Team Members

- Anurag (Database & Integration)
- [Your Teammate 1 Name] (API Endpoints)
- [Your Teammate 2 Name] (Testing & Docs)

---

## 🛠️ Requirements

- Python 3.10 or above
- MySQL Server
- VS Code or any code editor

Install required packages:

```bash
pip install fastapi uvicorn sqlalchemy pymysql


🗃️ MySQL Setup
Create a database and tables using MySQL Workbench or CLI:

CREATE DATABASE flight_booking;

USE flight_booking;

CREATE TABLE flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    airline VARCHAR(100),
    source VARCHAR(100),
    destination VARCHAR(100),
    departure VARCHAR(100),
    arrival VARCHAR(100),
    price INT
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(50)
);

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    flight_id INT,
    seats INT,
    status BOOLEAN,
    booked_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (flight_id) REFERENCES flights(id)
);


🔌 Configure DB in database.py
Edit your MySQL username and password in database.py:

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://username:password@localhost/flight_booking"

🚀 Running the API
Start the FastAPI server:

bash
Copy
Edit
uvicorn main:app --reload
Once started, open your browser:

👉 http://127.0.0.1:8000/docs — Interactive Swagger UI

Sample API Endpoints
➕ Add Flight (POST /flights)
json
Copy
Edit
{
  "airline": "Indigo",
  "source": "BLR",
  "destination": "DEL",
  "departure": "2025-08-10T07:00",
  "arrival": "2025-08-10T09:30",
  "price": 4500
}

📄 List Flights (GET /flights)
Returns all flight entries.

🔍 Search Flights (GET /flights/search?source=BLR&destination=DEL&date=2025-08-10)
Search flights by source, destination, and date.

🆔 Get Flight by ID (GET /flights/{id})
Returns flight matching given ID.

❌ Delete Flight (DELETE /flights/{id})
Removes the flight from database.
