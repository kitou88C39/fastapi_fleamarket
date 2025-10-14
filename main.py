from fastapi import FastAPI
from cruds import item
from routers import item

app = FastAPI()
app.include_router(item.router)

