from fastapi import APIRouter

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

USUARIOS_DB = []

@router.post("/login")
async def login(email: str, password: str):
    for u in USUARIOS_DB:
        if u["email"] == email:
            return {"success": True, "mensaje": "Inicio de sesión exitoso"}
    return {"success": False, "mensaje": "Usuario no encontrado"}
