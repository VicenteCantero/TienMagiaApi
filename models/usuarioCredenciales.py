from pydantic import BaseModel

# Login
class UsuarioCredenciales(BaseModel): 
    nombre: str
    password: str