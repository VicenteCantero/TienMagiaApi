from bson.objectid import ObjectId
from fastapi import APIRouter, Response
from models.cliente import Cliente
from config.db import conn
from schemas.clientesSchema import serializeCliente, serializeClienteList
from starlette.status import HTTP_204_NO_CONTENT

clienteRouter = APIRouter()
clienteCollection = conn.TiendaMagia.clientes

@clienteRouter.get('/', response_model=(list[Cliente]))
async def encuentra_todos_clientes():
    return serializeClienteList(clienteCollection.find())

@clienteRouter.post('/')
async def crear_cliente(cliente : Cliente):
    clienteCollection.insert_one(dict(cliente))
    return serializeClienteList(clienteCollection.find())

    ''' new_cliente =dict (cliente)
    del new_cliente["id"]
    id = clienteCollection.insert_one(new_cliente).inserted_id
    cliente = clienteCollection.find_one({"_id": ObjectId (id)})
    return serializeCliente(cliente)'''

@clienteRouter.get('/{id}')
async def encuentra_cliente_por_ID(id: str):
    return serializeCliente(clienteCollection.find_one({"_id": ObjectId(id)}))

@clienteRouter.put('/{id}')
async def actualiza_cliente(id: str, cliente: Cliente):
    clienteCollection.find_one_and_update({"_id": ObjectId(id)},{"$set": dict(cliente)})
    return serializeCliente(clienteCollection.find_one({"_id": ObjectId(id)}))

@clienteRouter.delete('/{id}')
async def borra_cliente(id: str):
    serializeCliente(clienteCollection.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code= HTTP_204_NO_CONTENT)
