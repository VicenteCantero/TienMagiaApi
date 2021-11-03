from bson.objectid import ObjectId
from fastapi import APIRouter, Response
from models.usuario import Usuario
from config.db import conn
from schemas.usuarioSchema import serializeUsuario, serializeUsuarioList
from starlette.status import HTTP_204_NO_CONTENT

usuarioRouter = APIRouter()
usuarioCollection = conn.TiendaMagia.usuarios

@usuarioRouter.get('/', response_model=(list[Usuario]))
async def encuentra_todos_usuarios():
    return serializeUsuarioList(usuarioCollection.find())

@usuarioRouter.post('/')
async def crear_usuario(usuario : Usuario):
    usuarioCollection.insert_one(dict(usuario))
    return serializeUsuarioList(usuarioCollection.find())

@usuarioRouter.get('/{id}')
async def encuentra_usuario_por_ID(id: str):
    return serializeUsuario(usuarioCollection.find_one({"_id": ObjectId(id)}))

@usuarioRouter.put('/{id}')
async def actualiza_usuario(id: str, usuario: Usuario):
    usuarioCollection.find_one_and_update({"_id": ObjectId(id)},{"$set": dict(usuario)})
    return serializeUsuario(usuarioCollection.find_one({"_id": ObjectId(id)}))

@usuarioRouter.delete('/{id}')
async def borra_usuario(id: str):
    serializeUsuario(usuarioCollection.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code= HTTP_204_NO_CONTENT)
