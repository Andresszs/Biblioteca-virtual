from fastapi import APIRouter

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

PEDIDOS_DB = []

@router.get("/historial/{usuario_id}")
async def historial(usuario_id: int):
    historial = [p for p in PEDIDOS_DB if p["usuario_id"] == usuario_id]
    return {"success": True, "historial": historial}
