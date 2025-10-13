from enum import Enum
from typing import Optional

class Item:
    def __init__(self, id: int, name: str, price: int, description: Optional[str], status: enum):