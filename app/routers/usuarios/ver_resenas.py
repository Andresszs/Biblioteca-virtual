from fastapi import APIRouter

router = APIRouter(prefix="/resenas", tags=["Reseñas"])

RESENAS_DB = []

@router.get("/ver/{libro_id}")
async def ver_resenas(libro_id: int):
    lista = [r for r in RESENAS_DB if r["libro_id"] == libro_id]
    return {"success": True, "resenas": lista}
