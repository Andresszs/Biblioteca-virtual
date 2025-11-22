from fastapi import APIRouter
from app.state import CART

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.get("/view")
async def view_cart():
    """
    HU07: Ver contenido del carrito.
    Retorna todos los libros agregados al carrito.
    """
    return {"cart": CART, "total_items": len(CART)}
