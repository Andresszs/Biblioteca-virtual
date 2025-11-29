from fastapi import APIRouter

router = APIRouter(prefix="/cupones", tags=["Cupones"])

CUPONES_DB = {
    "DESCUENTO10": 10,
    "LIBRO20": 20
}

@router.post("/aplicar")
async def aplicar_cupon(codigo: str, total_actual: float):
    if codigo not in CUPONES_DB:
        return {"success": False, "mensaje": "Cupón inválido"}

    descuento = CUPONES_DB[codigo]
    nuevo_total = total_actual - (total_actual * descuento / 100)

    return {
        "success": True,
        "mensaje": "Cupón aplicado",
        "descuento": descuento,
        "nuevo_total": nuevo_total
    }
