from bson.objectid import ObjectId
from fastapi import APIRouter, Response
from models.tipo import Tipo
from config.db import conn
from schemas.tipoSchema import serializeTipo, serializeTipoList
from starlette.status import HTTP_204_NO_CONTENT


tiposRouter = APIRouter()
tiposCollection = conn.TiendaMagia.tipo
productoCollection = conn.TiendaMagia.productos

@tiposRouter.get('/')
async def encuentra_todos_los_tipos():
    return serializeTipoList(tiposCollection.find())

@tiposRouter.get('/{id}')
async def encuentra_tipo_por_Id(id: str):
    return serializeTipo(tiposCollection.find_one({"_id": ObjectId(id)}))

@tiposRouter.get('/id/{id}')
async def esta_en_uso_tipo_por_Id(id: str):
    if productoCollection.find_one({"tipo": id})is not None:
        return True
    else:
        return False

@tiposRouter.get('/nombre/{nombre}')
async def existe_tipo_por_nombre(nombre: str):
    if tiposCollection.find_one({"nombre": nombre}) is not None:
        return True
    else:
        return False


@tiposRouter.post('/')
async def crear_tipo(tipo: Tipo):
    tiposCollection.insert_one(dict(tipo))
    return serializeTipoList(tiposCollection.find())

@tiposRouter.put('/{id}')
async def actualiza_tipo(id: str, tipo: Tipo):
    return serializeTipo(tiposCollection.find_one_and_update({"_id": ObjectId(id)},{"$set": dict(tipo)}))


@tiposRouter.delete('/{id}')
async def borra_tipo(id: str):
    serializeTipo(tiposCollection.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code= HTTP_204_NO_CONTENT)