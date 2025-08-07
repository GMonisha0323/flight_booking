from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import FlightCreate, FlightOut
import services
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/flights", response_model=List[FlightOut])
def list_flights(db: Session = Depends(get_db)):
    return services.get_all_flights(db)

@router.get("/flights/{flight_id}", response_model=FlightOut)
def get_flight(flight_id: int, db: Session = Depends(get_db)):
    flight = services.get_flight(db, flight_id)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight

@router.get("/flights/search", response_model=List[FlightOut])
def search(source: str, destination: str, date: str, db: Session = Depends(get_db)):
    return services.search_flights(db, source, destination, date)

@router.post("/flights", response_model=FlightOut)
def add_flight(flight: FlightCreate, db: Session = Depends(get_db)):
    return services.create_flight(db, flight)

@router.delete("/flights/{flight_id}", response_model=FlightOut)
def remove_flight(flight_id: int, db: Session = Depends(get_db)):
    flight = services.delete_flight(db, flight_id)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight
