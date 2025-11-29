from fastapi import APIRouter

router = APIRouter()

@router.get("/prestamos/activos")
def prestamos_activos():
    return {
        "mensaje": "Listado de préstamos activos",
        "prestamos": []  # Aquí en el futuro irán los datos reales
    }
