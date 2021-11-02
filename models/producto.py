from pydantic import BaseModel

class Producto(BaseModel):
    nombre: str
    precio: str
    tipo: str
    creador: str   
    descripcion: str
    alt_img: str
    cantidad: str
