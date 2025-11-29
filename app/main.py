from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routers.books.search_by_title import router as book_search_router
from app.routers.books.search_by_author import router as search_by_author_router
from app.routers.books.search_by_author import router as search_by_author_router
from app.routers.books.filter_by_category import router as book_filter_router
from app.routers.books.book_details import router as book_details_router
from app.routers.cart.add_to_cart import router as cart_add_router
from app.routers.cart.remove_from_cart import router as cart_remove_router
from app.routers.cart.view_cart import router as cart_view_router
from app.routers.cart.clear_cart import router as cart_clear_router
from app.routers.prestamos.registrar_prestamo import router as registrar_prestamo_router
from app.routers.prestamos.consultar_activos import router as prestamos_activos_router
from app.routers.prestamos.registrar_devolucion import router as registrar_devolucion_router
from app.routers.prestamos.registrar_devolucion import router as registrar_devolucion_router

from app.routers.multas.registrar_multa import router as registrar_multa_router
from app.routers.multas.consultar_multas_usuario import router as multas_usuario_router
from app.routers.usuarios.bloquear_usuario import router as bloquear_usuario_router
from app.routers.multas.pagar_multa import router as pagar_multa_router


app = FastAPI(
    title="Mi API con FastAPI",
    description="API RESTful profesional",
    version="1.0.0"
)

app.include_router(book_search_router)          # HU01
app.include_router(search_by_author_router)     # HU02
app.include_router(book_filter_router)          # HU03
app.include_router(book_details_router)         # HU04
app.include_router(cart_add_router)             # HU05
app.include_router(cart_remove_router)          # HU06
app.include_router(cart_view_router)            # HU07
app.include_router(cart_clear_router)           # HU08
app.include_router(registrar_prestamo_router, prefix="/api") # HU09
app.include_router(prestamos_activos_router, prefix="/api") # HU10
app.include_router(registrar_devolucion_router, prefix="/api") # HU11
app.include_router(registrar_devolucion_router, prefix="/api") # HU12

app.include_router(registrar_multa_router, prefix="/api") # HU14
app.include_router(multas_usuario_router, prefix="/api") # HU15
app.include_router(bloquear_usuario_router, prefix="/api") # HU16
app.include_router(pagar_multa_router, prefix="/api") # HU17

@app.get("/")
async def root():
    return {
        "message": "¡Bienvenido a mi API con FastAPI!",
        "status": "online",
        "version": "1.0.0"
    }

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.get("/health")
async def health_check():
    return JSONResponse(status_code=200, content={"status": "healthy"})
