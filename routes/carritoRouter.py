from bson.objectid import ObjectId
from fastapi import APIRouter, Response
from models.carrito import Carrito
from config.db import conn
from models.productoCarrito import ProductoCarrito
from schemas.carritoSchema import serializeCarrito,serializeCarritoList
from starlette.status import HTTP_204_NO_CONTENT


carritoRouter = APIRouter()
carritoCollection = conn.TiendaMagia.carrito

@carritoRouter.get('/')
def encuentra_carrito():
    return serializeCarrito(carritoCollection.find())

@carritoRouter.post('/')
def crear_carrito(carrito: Carrito):
    #Convertir el carrito a dict
    dictCarrito= dict(carrito)

    #coger los productos del carrito y borrarlos de él
    productos= dictCarrito.pop(['productoCarrito'], None)
    #pop elimina y devuelve
    #carrito.productoCarrito = None
    
    
    #convertir los productos a dict
    #[print(x) for x in thislist] 
    # mal = dictProductos= dict(productos)
    dictProductos = [dict(producto) for producto in productos]

    #guardar el carrito
    nuevaIdCarrito= carritoCollection.insert_one(dictCarrito)

    #asignar el id del nuevo carrito a los productos. recorrer= for elemento in diccionario
    for producto in dictProductos: 
        producto.carrito_id = nuevaIdCarrito


    #guardar los productos
    ProductosGuardado= carritoCollection.insert_many(dictProductos)

    return serializeCarrito (carritoCollection.find_one(({"_id": ObjectId(nuevaIdCarrito)})))

@carritoRouter.put('/')
def add_producto(productoCarrito: ProductoCarrito):
    return
