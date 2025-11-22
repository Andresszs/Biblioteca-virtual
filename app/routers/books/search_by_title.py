from fastapi import APIRouter, HTTPException, Query
from typing import List

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

BOOKS_DB = [
    {"id": 1, "title": "El Señor de los Anillos", "author": "J.R.R Tolkien"},
    {"id": 2, "title": "Cien Años de Soledad", "author": "Gabriel García Márquez"},
    {"id": 3, "title": "La Sombra del Viento", "author": "Carlos Ruiz Zafón"},
    {"id": 4, "title": "El Diario de Ana Frank", "author": "Ana Frank"},
    {"id": 5, "title": "El Principito", "author": "Antoine de Saint-Exupéry"}
]

@router.get("/search", summary="Buscar libros por título")
def search_books(title: str = Query(..., description="Título o parte del título del libro")):
    results = [book for book in BOOKS_DB if title.lower() in book["title"].lower()]
    
    if not results:
        raise HTTPException(status_code=404, detail="No se encontraron libros con ese título")
    
    return {"results": results}
