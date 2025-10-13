from fastapi import FastAPI
from cruds import item as item_cruds

app = FastAPI()

@app.get("/items")
async def find_all():
    return item_cruds.find_all()