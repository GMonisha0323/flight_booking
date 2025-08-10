from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from configs.database import Base

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    flight_id = Column(Integer, ForeignKey("flights.id"))
    confirmed = Column(Boolean, default=True)
    seats = Column(Integer)
    status = Column(String(50))
    booked_at = Column(String(50))

    user = relationship("User", back_populates="bookings")
    flight = relationship("Flight", back_populates="bookings")
