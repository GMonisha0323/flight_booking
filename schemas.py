from pydantic import BaseModel
from datetime import datetime

class FlightBase(BaseModel):
    airline: str
    source: str
    destination: str
    departure: str
    arrival: str
    price: int

class FlightCreate(FlightBase):
    pass

class FlightOut(FlightBase):
    id: int

    class Config:
        from_attributes = True

class BookingCreate(BaseModel):
    user_id: int
    flight_id: int
    seats: int
    status: str  # or Boolean
    booked_at: str
