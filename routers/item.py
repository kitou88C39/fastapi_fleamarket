from fastapi import APIRouter
from cruds import item as item_cruds

router = APIRouter()

@router.get("/items")
async def find_all():
    return item_cruds.find_all()