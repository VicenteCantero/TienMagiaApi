from pydantic import BaseModel

class ProductoCarrito(BaseModel):
    carrito_id: str   
    producto_id: str
    nombre: str
    precio: str
    cantidad: str