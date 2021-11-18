from bson.objectid import ObjectId
from fastapi import APIRouter, Response
from models.producto import Producto
from config.db import conn
from schemas.productosSchema import serializeProducto, serializeProductoList
from starlette.status import HTTP_204_NO_CONTENT

from schemas.tipoSchema import serializeTipo


productoRouter = APIRouter()
productoCollection = conn.TiendaMagia.productos
tipoCollection = conn.TiendaMagia.tipo

@productoRouter.get('/')
async def encuentra_todos_productos():
    #paños-objeto= funcion-mama hacer paños (camisetas viejas-objeto)
    listaProductos = serializeProductoList(productoCollection.find())

    for producto in listaProductos:
        tipo = serializeTipo( tipoCollection.find_one({"_id": ObjectId(producto["tipo"])}))
        producto["tipo"] = tipo["nombre"]
        
    return  listaProductos


@productoRouter.get('/{id}')
async def encuentra_producto_por_Id(id: str):
    return serializeProducto(productoCollection.find_one({"_id": ObjectId(id)}))

@productoRouter.get('/nombre/{nombre}')
async def encuentra_producto_por_nombre(nombre: str):
    return serializeProducto(productoCollection.find_one({"nombre": nombre}))

@productoRouter.get('/tipo/{tipo}')
async def encuentra_producto_por_tipo(tipo: str):
    return serializeProducto(productoCollection.find_one({"tipo": tipo}))

@productoRouter.post('/')
async def crear_producto(producto: Producto):
    productoCollection.insert_one(dict(producto))
    return serializeProductoList(productoCollection.find())

@productoRouter.put('/{id}')
async def actualiza_producto(id: str, producto: Producto):
    return serializeProducto(productoCollection.find_one_and_update({"_id": ObjectId(id)},{"$set": dict(producto)}))

@productoRouter.delete('/{id}')
async def borra_producto(id: str):
    serializeProducto(productoCollection.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code= HTTP_204_NO_CONTENT)