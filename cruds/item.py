from sqlalchemy.orm import Session
from schemas import ItemCreate, ItemStatus
from models import Item


def find_all(db: Session):
    return db.query(Item).all()


def find_by_id(db: Session, id: int):
    return db.query(Item).filter(Item.id == id).first()
    

def find_by_name(db: Session, name: str):
    return db.query(Item).filter(Item.name.like(f"%{name}%")).all()
    

def create(db: Session, item_create: ItemCreate):
    new_item = Item(
        **item_create.model_dump()
    )
    db.add(new_item)
    db.commit()
    return new_item

def update(db: Session, id: int, item_update: ItemUpdate):
    item = find_by_id(db, id)
    if item is None:
        return None

    item.name = item_update if item_update.name is None else item_update.name
    item.price = item_update if item_update.price is None else item_update.price
    item.description = (
        item.description if item_update.description is None else item_update.description
    )
    item.status = (
        item.status if item_update.status is None else item_update.status
    )
    db.add(item)
    db.commit()

    return item


# def delete(id: int):
#     for i in range(len(items)):
#         if items[i].id == id:
#             deleted_item = items.pop(i)
#             return deleted_item
#     return None