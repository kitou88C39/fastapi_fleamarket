from fastapi import FastAPI,Body
from cruds import item as item_cruds
from routers import item

app = FastAPI()
app.include_router(item.router)

