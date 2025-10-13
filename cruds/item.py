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
