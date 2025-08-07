from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

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


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    phone = Column(String(50))
    bookings = relationship("Booking", back_populates="user")


class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    flight_id = Column(Integer, ForeignKey("flights.id"))
    confirmed = Column(Boolean, default=True)

    user = relationship("User", back_populates="bookings")
    flight = relationship("Flight", back_populates="bookings")
