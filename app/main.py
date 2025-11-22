from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routers.books.search_by_title import router as book_search_router
from app.routers.books.search_by_author import router as search_by_author_router
from app.routers.books.search_by_author import router as search_by_author_router
from app.routers.books.filter_by_category import router as book_filter_router


app = FastAPI(
    title="Mi API con FastAPI",
    description="API RESTful profesional",
    version="1.0.0"
)

app.include_router(book_search_router)          # HU01
app.include_router(search_by_author_router)     # HU02
app.include_router(book_filter_router)



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
