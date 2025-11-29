from fastapi import APIRouter

router = APIRouter()

@router.get("/multas/usuario/{usuario_id}")
def multas_usuario(usuario_id: int):
    return {
        "mensaje": "Multas del usuario",
        "usuario": usuario_id,
        "multas": []
    }
