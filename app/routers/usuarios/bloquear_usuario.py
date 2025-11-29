from fastapi import APIRouter

router = APIRouter()

@router.put("/usuarios/bloquear/{usuario_id}")
def bloquear_usuario(usuario_id: int):
    return {
        "mensaje": "Usuario bloqueado por multas pendientes",
        "usuario": usuario_id
    }
