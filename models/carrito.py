from pydantic import BaseModel

from models.productoCarrito import ProductoCarrito

class Carrito(BaseModel):
    usu_id: str
    #fecha: str
    productoCarrito:list [ProductoCarrito]
    total: str