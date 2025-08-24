import fastapi
import uvicorn
from pydantic import BaseModel

app = fastapi.FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}", "price": 10.0 * item_id}

@app.post("/items")
async def create_item(item: Item):
    return {"message": "Item criado com sucesso", "item": item}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
