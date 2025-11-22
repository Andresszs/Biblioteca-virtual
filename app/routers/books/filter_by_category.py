from fastapi import APIRouter, Query

router = APIRouter(prefix="/books", tags=["Books"])

# Datos simulados
BOOKS = [
    {"id": 1, "title": "El Principito", "author": "Antoine de Saint-Exupéry", "category": "novela"},
    {"id": 2, "title": "Cien Años de Soledad", "author": "Gabriel García Márquez", "category": "realismo mágico"},
    {"id": 3, "title": "Python Profesional", "author": "Guido Rossum", "category": "programación"},
    {"id": 4, "title": "Clean Code", "author": "Robert C. Martin", "category": "programación"},
    {"id": 5, "title": "Los Miserables", "author": "Victor Hugo", "category": "novela"}
]

@router.get("/filter")
async def filter_books_by_category(category: str = Query(..., description="Categoría del libro")):
    results = [book for book in BOOKS if category.lower() in book["category"].lower()]
    return {"results": results}

