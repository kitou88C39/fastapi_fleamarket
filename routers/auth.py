from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from cruds import auth as auth_cruds
from schemas import UserCreate, UserResponse
from database import get_db