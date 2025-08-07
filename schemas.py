from pydantic import BaseModel

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
