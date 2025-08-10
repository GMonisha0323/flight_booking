from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from configs.database import get_db
from services import booking_service
from schemas.booking_schema import BookingCreate  
from typing import List
from schemas.booking_schema import BookingOut



router = APIRouter()

@router.post("/bookings")
def book_flight(booking: BookingCreate, db: Session = Depends(get_db)):
    return booking_service.create_booking(db, booking)

@router.get("/bookings", response_model=List[BookingOut])
def get_bookings(db: Session = Depends(get_db)):
    return booking_service.get_all_bookings(db)

@router.delete("/bookings/{booking_id}", response_model=BookingOut)
def remove_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = booking_service.delete_booking(db, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking
