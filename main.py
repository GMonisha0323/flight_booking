from fastapi import FastAPI
from database import Base, engine
from controller import router

app = FastAPI(title="✈️ Flight Search API with MySQL")

# Create tables if not exists
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Flight API is running"}

app.include_router(router)
