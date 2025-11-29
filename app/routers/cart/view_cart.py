from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/cart", tags=["Cart"])

# Carrito en memoria
CART = [
    {"book_id": 1, "titulo": "Libro A", "precio": 30000, "cantidad": 2},
    {"book_id": 2, "titulo": "Libro B", "precio": 45000, "cantidad": 1}
]


@router.get("/view")
async def view_cart(test_case: int = 1):
    """
    test_case:
    1 = Carrito con items
    2 = Carrito vacío
    3 = Validación de cálculos
    4 = Usuario no autenticado
    5 = Error de base de datos
    """

    # --------------------------------------------------------------------
    # ❌ Caso 4: Usuario NO autenticado
    # --------------------------------------------------------------------
    if test_case == 4:
        return JSONResponse(
            status_code=401,
            content={
                "success": False,
                "mensaje": "Autenticación requerida"
            }
        )

    # --------------------------------------------------------------------
    # ❌ Caso 5: Error de base de datos simulado
    # --------------------------------------------------------------------
    if test_case == 5:
        return JSONResponse(
            status_code=503,
            content={
                "success": False,
                "mensaje": "No fue posible obtener el carrito"
            }
        )

    # --------------------------------------------------------------------
    # ✔ Caso 2: Carrito vacío
    # --------------------------------------------------------------------
    if test_case == 2:
        return {
            "success": True,
            "mensaje": "El carrito está vacío",
            "items": [],
            "subtotal": 0,
            "descuento": 0,
            "envio": 0,
            "total": 0,
            "total_items": 0
        }

    # --------------------------------------------------------------------
    # ✔ Caso 1 y 3 (mismos cálculos, cambia solo el propósito)
    # --------------------------------------------------------------------
    carrito = CART if test_case in (1, 3) else []

    subtotal = sum(item["precio"] * item["cantidad"] for item in carrito)
    descuento = 0
    envio = 0
    total = subtotal - descuento + envio
    total_items = sum(item["cantidad"] for item in carrito)

    return {
        "success": True,
        "mensaje": "Carrito obtenido correctamente",
        "items": carrito,
        "subtotal": subtotal,
        "descuento": descuento,
        "envio": envio,
        "total": total,
        "total_items": total_items
    }
