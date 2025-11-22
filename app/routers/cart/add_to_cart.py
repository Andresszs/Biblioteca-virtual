from fastapi import APIRouter

router = APIRouter(prefix="/cart", tags=["Cart"])

CART = []

@router.post("/add")
async def add_to_cart(book_id: int):
    CART.append({"book_id": book_id, "quantity": 1})
    return {"message": "Libro agregado al carrito", "cart": CART}
