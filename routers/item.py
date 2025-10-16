from typing import Optional
from fastapi import APIRouter, Path, Query
from cruds import item as item_cruds
from schemas import ItemCreate, ItemUpdate, ItemResponse

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("", response_model=list[ItemResponse])
async def find_all():
    return item_cruds.find_all()

@router.get("/{id}", response_model=Optional[ItemResponse])
async def find_by_id(id: int=Path(gt=0)):
    return item_cruds.find_by_id(id)

@router.get("/", response_model=list[ItemResponse])
async def find_by_name(name: str = Query(min_length=2, max_length=20)):
    return item_cruds.find_by_name(name)

@router.post("", response_model=ItemResponse)
async def create(item_create: ItemCreate):
    return item_cruds.create_item(item_create)

@router.put("/{id}", response_model=Optional[ItemResponse])
async def update(item_update: ItemUpdate, id: int = Path(gt=0)):
    return item_cruds.update(id, item_update)

@router.delete("/{id}", response_model=Optional[ItemResponse])
async def delete(id: int = Path(gt=0)):
    return item_cruds.delete(id)