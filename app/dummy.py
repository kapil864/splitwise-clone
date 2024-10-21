from core.db import user_collection

from fastapi import APIRouter
from pydantic import BaseModel

dummy_router = APIRouter(prefix='/dummy')


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    quantity: int


@dummy_router.post("/items/")
async def create_item(item: Item):
    result = await user_collection.insert_one(item.model_dump())
    document = await user_collection.find_one()
    document["_id"] = str(document["_id"])
    return {"id": str(result.inserted_id), "object": document}
