from pydantic import BaseModel
from typing import Optional

class BookingCreate(BaseModel):
    user_id: int
    flight_id: int
    seats: int
    status: str
    booked_at: str


class BookingOut(BaseModel):
    id: int
    user_id: int
    flight_id: int
    seat_number: Optional[str] = None
