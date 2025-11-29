# app/state.py - estado en memoria para pruebas
from datetime import datetime

# libros de ejemplo (id como str)
BOOKS = [
    {"id": "5001", "title": "Libro Prueba", "price": 30000, "stock": 10},
    {"id": "2002", "title": "Libro 2", "price": 15000, "stock": 1},
]

USERS = []      # usuarios registrados
SESSIONS = {}   # token -> usuario_id (login simple)
ORDERS = []     # pedidos
COUPONS = [     # cupones de prueba
    {"code": "DESC10", "type": "percent", "value": 10, "active": True},
    {"code": "FIVEOFF", "type": "fixed", "value": 5000, "active": True},
]
REVIEWS = []    # reseñas: {id, book_id, user_id, rating, comment, date}
CART = []
