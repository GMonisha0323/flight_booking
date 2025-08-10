from fastapi import APIRouter, Depends, HTTPException  # ✅ Added HTTPException
from sqlalchemy.orm import Session
from configs.database import get_db
from services import flight_service
from typing import List
from schemas.flight_schema import FlightOut, FlightCreate  # ✅ Correct imports

router = APIRouter()

@router.get("/flights", response_model=List[FlightOut])
def list_flights(db: Session = Depends(get_db)):
    return flight_service.get_all_flights(db)

@router.get("/flights/{flight_id}", response_model=FlightOut)
def get_flight(flight_id: int, db: Session = Depends(get_db)):
    flight = flight_service.get_flight(db, flight_id)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight

@router.post("/flights", response_model=FlightOut)
def add_flight(flight: FlightCreate, db: Session = Depends(get_db)):
    return flight_service.create_flight(db, flight)

@router.delete("/flights/{flight_id}", response_model=FlightOut)
def remove_flight(flight_id: int, db: Session = Depends(get_db)):
    flight = flight_service.delete_flight(db, flight_id)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight
