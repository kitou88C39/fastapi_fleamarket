from enum import Enum
from typing import Optional
from schemas import ItemCreate

# class ItemStatus(Enum):
#     ON_SALE = "on_sale"
#     SOLD_OUT = "sold_out"
class Item:
    def __init__(
        self, 
        id: int, 
        name: str, 
        price: int, 
        description: Optional[str], 
        status: ItemStatus
    ):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.status = status

items = [
    Item(1, "PC", 100, "備品です", ItemStatus.ON_SALE),
    Item(2, "スマートフォン", 200, None, ItemStatus.ON_SALE),
    Item(3, "本", 300, "使用感あり", ItemStatus.SOLD_OUT),
]

def find_all():
    return items

def find_by_id(id: int):
    for item in items:
        if item.id == id:
            return item
    return None

def find_by_name(name: str):
    filtered_items = []

    for item in items:
        if name in item.name:
            filtered_items.append(item)
    return filtered_items

def create(item_create: ItemCreate):
    new_item = Item(
        len(items) + 1,
        item_create.name,
        item_create.price,
        item_create.description,
        ItemStatus.ON_SALE,
    )    
    items.append(new_item)
    return new_item

def update(id: int, item_update):
    for item in items:
        if item.id == id:
            item.name = item_update.get("name", item.name)
            item.price = item_update.get("price", item.price)
            item.description = item_update.get("description", item.description)
            item.status = item_update.get("status", item.status)    
            return item
    return None


def delete(id: int):
    for i in range(len(items)):
        if items[i].id == id:
            deleted_item = items.pop(i)
            return deleted_item
    return None