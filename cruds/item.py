from sqlalchemy.orm import Session
from schemas import ItemCreate, ItemStatus
from models import Item


# def find_all():
#     return items

# def find_by_id(id: int):
#     for item in items:
#         if item.id == id:
#             return item
#     return None

# def find_by_name(name: str):
#     filtered_items = []

#     for item in items:
#         if name in item.name:
#             filtered_items.append(item)
#     return filtered_items

def create(db: Session, item_create: ItemCreate):
    new_item = Item(
        **item_create.model_dump()
    )
    db.add(new_item)
    db.commit()
    return new_item

# def update(id: int, item_update: ItemUpdate):
#     for item in items:
#         if item.id == id:
#             item.name = item_update if item_update.name is None else item_update.name
#             item.price = item_update if item_update.price is None else item_update.price
#             item.description = item_update if item_update.description is None else item_update.description
#             item.status = item_update if item_update.status is None else item_update.status  
#             return item
#     return None


# def delete(id: int):
#     for i in range(len(items)):
#         if items[i].id == id:
#             deleted_item = items.pop(i)
#             return deleted_item
#     return None