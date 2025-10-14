from fastapi import APIRouter
from cruds import item

router = APIRouter()

@router.get("/items")
async def find_all():
    return item.find_all()