import hashlib
import base64
import os
from sqlalchemy import Session
from schemas import UserCreate
from models import User


def create(db: Session, user_create: UserCreate):
    salt = base64.b64encode(os.urandom(32))
    hash_password = hashlib.pbkdf2_hmac("sha256", user_create.password.encode(), salt, 1000).hex()
    new_user = User(
        username=user_create.username,
        password=hash_password,
        email=user_create.email,
        salt=salt.decode()
    )
    db.add(new_user)
    db.commit()

    return new_user

    def authenticate(db: Session, username: str, password: str):