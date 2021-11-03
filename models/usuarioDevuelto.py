from pydantic import BaseModel

# respuesta del Login (get datos usuario)
class UsuarioDevuelto(BaseModel): 
    nombre: str
    email: str