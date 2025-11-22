from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/books", tags=["Books"])

BOOKS = [
    {"id": 1, "title": "El Principito", "author": "Antoine de Saint-Exupéry", "category": "novela"},
    {"id": 2, "title": "Cien Años de Soledad", "author": "Gabriel García Márquez", "category": "realismo mágico"},
    {"id": 3, "title": "Python Profesional", "author": "Guido Rossum", "category": "programación"},
]

@router.get("/details/{book_id}")
async def get_book_details(book_id: int):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Libro no encontrado")
