"""Módulo principal para a API de itens, usando FastAPI."""

import fastapi
import uvicorn
from pydantic import BaseModel

app = fastapi.FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
async def read_root():
    """A simple endpoint that returns a greeting message."""
    return {"Hello": "Mundo"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """Endpoint to get an item by its ID."""
    return {"item_id": item_id, "name": f"Item {item_id}", "price": 10.0 * item_id}

@app.post("/items")
async def create_item(item: Item):
    """Endpoint to create a new item."""
    return {"message": "Item criado com sucesso", "item": item}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
