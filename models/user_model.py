from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from configs.database import Base  # ✅ FIX wrong import path

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    phone = Column(String(50))

    bookings = relationship("Booking", back_populates="user")
