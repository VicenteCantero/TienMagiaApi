from pydantic import BaseModel


class Cliente(BaseModel): 
    nombre: str
    email: str
    password: str

