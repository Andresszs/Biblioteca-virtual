from fastapi import APIRouter

router = APIRouter(prefix="/resenas", tags=["Reseñas"])

RESENAS_DB = []

@router.post("/agregar")
async def agregar_resena(libro_id: int, usuario_id: int, calificacion: int, comentario: str):
    res = {
        "id": len(RESENAS_DB)+1,
        "libro_id": libro_id,
        "usuario_id": usuario_id,
        "calificacion": calificacion,
        "comentario": comentario
    }
    RESENAS_DB.append(res)
    return {"success": True, "resena": res}
