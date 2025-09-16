"""Módulo principal da API que define os endpoints."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    """Modelo de dados para um item."""
    name: str
    price: float

@app.get("/")
async def read_root():
    """Um endpoint simples que retorna uma mensagem de saudação."""
    return {"Hello": "Mundo"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """Endpoint para obter um item pelo seu ID."""
    return {"item_id": item_id, "name": f"Item {item_id}", "price": 10.0 * item_id}

@app.post("/items/")
async def create_item(item: Item):
    """Endpoint para criar um novo item."""
    return {"message": "Item criado com sucesso", "item": item.model_dump()}
