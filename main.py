from fastapi import FastAPI
from configs.database import Base, engine
from controllers import flight_controller, booking_controller, user_controller

# Create FastAPI app
app = FastAPI(title='FLIGHT_BOOKING_API')

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Flight API is running"}

# Include routers
app.include_router(flight_controller.router, tags=["Flights"])
app.include_router(user_controller.router, tags=["Users"])
app.include_router(booking_controller.router, tags=["Bookings"])
