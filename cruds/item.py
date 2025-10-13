from enum import Enum
from typing import Optional


class ItemStatus(Enum):
    ON_SALE = "on_sale"
    SOLD_OUT = "sold_out"
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