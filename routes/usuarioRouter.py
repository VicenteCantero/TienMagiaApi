from bson.objectid import ObjectId
from fastapi import APIRouter, Response
from fastapi.exceptions import HTTPException
from config.autorizacionHandler import AutorizacionHandler
from models.usuario import Usuario
from config.db import conn
from schemas.usuarioDevueltoSchema import serializeUsuarioDevuelto
from schemas.usuarioSchema import serializeUsuario, serializeUsuarioList
from starlette.status import HTTP_204_NO_CONTENT

usuarioRouter = APIRouter()
usuarioCollection = conn.TiendaMagia.usuarios

autorizacionHandler= AutorizacionHandler ()

@usuarioRouter.post('/registro')
def registrarUsuario(usuario:Usuario):
    nombreRepetido = usuarioCollection.find_one({"nombre": usuario.nombre})
    if nombreRepetido is not None:
        raise HTTPException (status_code= 400, detail="Nombre repetido")
    passwordEncriptado = autorizacionHandler.encriptarPassword(usuario.password)
    usuario.password = passwordEncriptado
    usuarioCollection.insert_one(dict(usuario))
    return serializeUsuarioDevuelto(usuarioCollection.find_one({"nombre": usuario.nombre}))

