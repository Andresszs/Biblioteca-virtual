from fastapi import APIRouter

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

PEDIDOS_DB = []

@router.post("/procesar")
async def procesar_pedido(usuario_id: int, total: float):
    pedido = {"id": len(PEDIDOS_DB)+1, "usuario_id": usuario_id, "total": total}
    PEDIDOS_DB.append(pedido)
    return {"success": True, "mensaje": "Pedido procesado", "pedido": pedido}
