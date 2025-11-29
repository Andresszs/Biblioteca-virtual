from fastapi import APIRouter

router = APIRouter()

@router.put("/prestamos/devolver/{prestamo_id}")
def registrar_devolucion(prestamo_id: int):
    return {
        "mensaje": "Devolución registrada",
        "prestamo": prestamo_id,
        "estado": "finalizado"
    }
