import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="", port=8000)

