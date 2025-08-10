from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from configs.database import get_db
from services import user_service
from schemas.user_schema import UserCreate, UserOut  # ✅ Missing imports
from models.user_model import User
from typing import List


router = APIRouter()

@router.post("/users", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)


@router.get("/users", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)


@router.delete("/users/{user_id}", response_model=UserOut)
def remove_user (user_id: int, db: Session = Depends(get_db)):
    users = user_service.delete_user(db, user_id)
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    return users