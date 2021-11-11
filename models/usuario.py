from pydantic import BaseModel

# registro
class Usuario(BaseModel): 
    nombre: str
    email: str
    password: str



