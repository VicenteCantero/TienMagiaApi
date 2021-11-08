from bson.objectid import ObjectId
from fastapi import APIRouter, Response
from fastapi.exceptions import HTTPException
from config.autorizacionHandler import AutorizacionHandler
from models.usuario import Usuario
from config.db import conn
from models.usuarioCredenciales import UsuarioCredenciales
from schemas.usuarioDevueltoSchema import serializeUsuarioDevuelto
from schemas.usuarioSchema import serializeUsuario, serializeUsuarioList
from starlette.status import HTTP_204_NO_CONTENT

usuarioRouter = APIRouter()
usuarioCollection = conn.TiendaMagia.usuarios

autorizacionHandler= AutorizacionHandler ()

@usuarioRouter.post('/registro')
def registrarUsuario(usuario:Usuario):
    usuarioExistente = usuarioCollection.find_one({"nombre": usuario.nombre})
    if usuarioExistente is not None:
        raise HTTPException (status_code= 400, detail="Nombre repetido")
    passwordEncriptado = autorizacionHandler.encriptarPassword(usuario.password)
    usuario.password = passwordEncriptado
    usuarioCollection.insert_one(dict(usuario))
    return serializeUsuarioDevuelto(usuarioCollection.find_one({"nombre": usuario.nombre}))


@usuarioRouter.post('/login')
def loginUsuario(usuario : UsuarioCredenciales):
    usuarioExistente = usuarioCollection.find_one ({"nombre": usuario.nombre}) 
    if usuarioExistente is None:
        raise  HTTPException (status_code= 400, detail="No existe ese usuario")
    verificarP = autorizacionHandler.verificarPassword(usuario.password, usuarioExistente["password"])
    if not verificarP:
        raise  HTTPException (status_code= 400, detail="Password incorrecto")
    token= autorizacionHandler.codificarToken(usuarioExistente["nombre"])
    return {'token': token, 'username': usuarioExistente["nombre"], 'id': str (usuarioExistente["_id"])}