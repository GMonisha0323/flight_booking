from models.flight_model import Flight
from sqlalchemy.orm import Session
from schemas.flight_schema import FlightCreate



def get_all_flights(db: Session):
    return db.query(Flight).all()

def get_flight(db: Session, flight_id: int):
    return db.query(Flight).filter(Flight.id == flight_id).first()

def search_flights(db: Session, source: str, destination: str):
    return db.query(Flight).filter(
        Flight.source == source,
        Flight.destination == destination
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
