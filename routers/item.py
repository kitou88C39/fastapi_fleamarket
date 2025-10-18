from typing import Annotated
from fastapi import APIRouter, Path, Query, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
from cruds import item as item_cruds
from schemas import ItemCreate, ItemUpdate, ItemResponse
from database import get_db

DbDependency = Annotated[Session, Depends(get_db)]


router = APIRouter(prefix="/items", tags=["Items"])

@router.get("", response_model=list[ItemResponse])
async def find_all(db: DbDependency):
    return item_cruds.find_all(db)

# @router.get("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
# async def find_by_id(id: int=Path(gt=0)):
#     found_item = item_cruds.find_by_id(id)
#     if not found_item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return found_item

# @router.get("/", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
# async def find_by_name(name: str = Query(min_length=2, max_length=20)):
#     return item_cruds.find_by_name(name)

@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create(db: DbDependency, item_create: ItemCreate):
    return item_cruds.create_item(db, item_create)

# @router.put("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
# async def update(item_update: ItemUpdate, id: int = Path(gt=0)):
#     update_item = item_cruds.update(id, item_update)
#     if not update_item:
#         raise HTTPException(status_code=404, detail="Item not updated")
#     return update_item

# @router.delete("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
# async def delete(id: int = Path(gt=0)):
#     delete_item = item_cruds.delete(id)
#     if not delete_item:
#         raise HTTPException(status_code=404, detail="Item not deleted")
#     return delete_item