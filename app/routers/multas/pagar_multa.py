from fastapi import APIRouter

router = APIRouter()

@router.put("/multas/pagar/{multa_id}")
def pagar_multa(multa_id: int):
    return {
        "mensaje": "Multa pagada",
        "multa": multa_id,
        "estado": "pagada"
    }
