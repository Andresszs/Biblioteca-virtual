from fastapi import APIRouter

router = APIRouter(prefix="/cart", tags=["Cart"])

CART = []

@router.delete("/remove/{book_id}")
async def remove_from_cart(book_id: int):
    global CART
    CART = [item for item in CART if item["book_id"] != book_id]
    return {"message": "Libro eliminado", "cart": CART}
