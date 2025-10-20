from datetime import datetime, timedelta
import hashlib
import base64
import os
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, oauth2
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from schemas import UserCreate
from models import User


ALGORITHM = "HS256"
SECRET_KEY = "df03e14f52bca218e6fe263876108d19df46e92046900c0666e4135f54dc8f9c"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def create(db: Session, user_create: UserCreate):
    salt = base64.b64encode(os.urandom(32))
    hash_password = hashlib.pbkdf2_hmac(
        "sha256", user_create.password.encode(), salt, 1000
        ).hex()
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
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None

    hash_password = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), user.salt, 1000
        ).hex()
    if hash_password != user.password:
        return None

    return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    expires = datetime.now() + expires_delta
    payload = {
        "sub": username,
        "id": user_id,
        "exp": expires
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        user_id = payload.get("id")
        if username is None or user_id is None:
            return Nome

    except JWTError:
        raise JWTError("")
    