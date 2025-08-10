from sqlalchemy.orm import Session  # ✅ Missing import
from models.user_model import User
from schemas.user_schema import UserCreate

def create_user(db: Session, user: UserCreate):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#def get_user(db: Session, user_id: int):
    #return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session):
    return db.query(User).all()

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return user
    return None

