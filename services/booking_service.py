from sqlalchemy.orm import Session  # ✅ Missing import
from models.booking_model import Booking
from schemas.booking_schema import BookingCreate

def create_booking(db: Session, booking: BookingCreate):
    new_booking = Booking(**booking.dict())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

def get_all_bookings(db: Session):
    return db.query(Booking).all()

def delete_booking(db: Session, booking_id: int):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if booking:
        db.delete(booking)
        db.commit()
        return booking
    return None
