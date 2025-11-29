from fastapi import APIRouter

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

PEDIDOS_DB = []

@router.get("/detalle/{pedido_id}")
async def detalle(pedido_id: int):
    for p in PEDIDOS_DB:
        if p["id"] == pedido_id:
            return {"success": True, "pedido": p}
    return {"success": False, "mensaje": "Pedido no encontrado"}
