from fastapi import APIRouter, Body
from cruds import item as item_cruds

router = APIRouter(prefix="/items")

@router.get("")
async def find_all():
    return item_cruds.find_all()

@router.get("")
async def find_all():
    return item_cruds.find_all()

@router.get("/{id}")
async def find_by_id(id: int):
    return item_cruds.find_by_id(id)

@router.get("/")
async def find_by_name(name: str):
    return item_cruds.find_by_name(name)

@router.post("")
async def create(item_create=Body()):
    return item_cruds.create_item(item_create)

@router.put("/{id}")
async def update(id: int, item_update=Body()):
    return item_cruds.update(id, item_update)

@router.delete("/{id}")
async def delete(id: int):
    return item_cruds.delete(id)