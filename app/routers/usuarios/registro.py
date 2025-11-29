from fastapi import APIRouter

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

USUARIOS_DB = []

@router.post("/registro")
async def registrar_usuario(nombre: str, email: str, password: str):
    for u in USUARIOS_DB:
        if u["email"] == email:
            return {"success": False, "mensaje": "El correo ya está registrado"}

    nuevo = {"id": len(USUARIOS_DB)+1, "nombre": nombre, "email": email}
    USUARIOS_DB.append(nuevo)

    return {"success": True, "mensaje": "Usuario registrado", "usuario": nuevo}
