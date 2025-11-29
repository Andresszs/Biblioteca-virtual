from fastapi import APIRouter

router = APIRouter()

@router.post("/prestamos/registrar")
def registrar_prestamo(usuario_id: int, libro_id: int, fecha_prestamo: str, fecha_devolucion_estimada: str):
    return {
        "mensaje": "Préstamo registrado correctamente",
        "usuario": usuario_id,
        "libro": libro_id,
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion_estimada": fecha_devolucion_estimada
    }
