from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from configs.database import Base

class Flight(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True, index=True)
    airline = Column(String(100))
    source = Column(String(100))
    destination = Column(String(100))
    departure = Column(String(100))
    arrival = Column(String(100))
    price = Column(Integer)

    bookings = relationship("Booking", back_populates="flight")
