from fastapi import APIRouter, Query

router = APIRouter(prefix="/books", tags=["Books"])

# Base de datos simulada
BOOKS_DB = [
    {"id": 1, "title": "Cien años de soledad", "author": "Gabriel García Márquez", "category": "Realismo mágico"},
    {"id": 2, "title": "El coronel no tiene quien le escriba", "author": "Gabriel García Márquez", "category": "Realismo mágico"},
    {"id": 3, "title": "Rayuela", "author": "Julio Cortázar", "category": "Ficción"},
    {"id": 4, "title": "Ficciones", "author": "Jorge Luis Borges", "category": "Filosofía"},
    {"id": 5, "title": "El Principito", "author": "Antoine de Saint-Exupéry", "category": "Infantil"},
]

@router.get("/search-by-author")
async def search_by_author(author: str = Query(..., min_length=2, description="Nombre del autor")):
    results = [book for book in BOOKS_DB if author.lower() in book["author"].lower()]
    return {"results": results}
