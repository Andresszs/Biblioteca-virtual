from fastapi import APIRouter

router = APIRouter()

@router.post("/multas/registrar")
def registrar_multa(prestamo_id: int, dias_retraso: int):
    monto = dias_retraso * 1000  # ejemplo
    return {
        "mensaje": "Multa registrada",
        "prestamo_id": prestamo_id,
        "dias_retraso": dias_retraso,
        "monto": monto
    }
