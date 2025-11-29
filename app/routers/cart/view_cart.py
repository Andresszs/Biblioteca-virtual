from fastapi import APIRouter

router = APIRouter(prefix="/cart", tags=["Cart"])

CART = []

@router.get("/view")
async def view_cart():
    return {"cart": CART}

