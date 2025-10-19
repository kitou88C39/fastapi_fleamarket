from sqlalchemy import Session
from schemas import UserCreate
from models import User


def create(db: Session, user_create: UserCreate):
    new_user = User(username=user_create.username,)
    db.add(new_user)
    db.commit()
    
    return new_user