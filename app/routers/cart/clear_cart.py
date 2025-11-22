from fastapi import APIRouter
from app.state import CART

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.delete("/clear")
async def clear_cart():
    """
    HU08: Vaciar el carrito.
    Limpia completamente el carrito.
    """
    CART.clear()
    return {"message": "Carrito vaciado exitosamente", "cart": CART}
