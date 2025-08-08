from sqlalchemy.orm import Session
from models import Flight
from schemas import FlightCreate
from models import Booking
from schemas import BookingCreate

def get_all_flights(db: Session):
    return db.query(Flight).all()

def get_flight(db: Session, flight_id: int):
    return db.query(Flight).filter(Flight.id == flight_id).first()

def search_flights(db: Session, source: str, destination: str, date: str):
    return db.query(Flight).filter(
        Flight.source == source,
        Flight.destination == destination,
        Flight.date.startswith(date)
    ).all()

def create_flight(db: Session, flight: FlightCreate):
    new_flight = Flight(**flight.dict())
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    return new_flight

def delete_flight(db: Session, flight_id: int):
    flight = db.query(Flight).filter(Flight.id == flight_id).first()
    if flight:
        db.delete(flight)
        db.commit()
    return flight



def create_booking(db: Session, booking: BookingCreate):
    new_booking = Booking(**booking.dict())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

