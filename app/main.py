from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Mi API con FastAPI",
    description="API RESTful profesional",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "¡Bienvenido a mi API con FastAPI!",
        "status": "online",
        "version": "1.0.0"
    }

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.get("/health")
async def health_check():
    return JSONResponse(status_code=200, content={"status": "healthy"})
