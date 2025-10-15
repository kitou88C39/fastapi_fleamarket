from typing import Optional
from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=20, examples=["PC"])
    price: int = Field(gt=0, examples=[10000])
    description: Optional[str] = Field(None, examples=["備品です"])
