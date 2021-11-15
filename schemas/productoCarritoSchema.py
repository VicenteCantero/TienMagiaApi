def serializeProductoCarrito(item) -> dict:

    return {
        "id": str (item["_id"]),
        "carrito_id": item["carrito_id"],
        "producto_id": item["producto_id"],
        "nombre": item["nombre"],
        "precio":item["precio"],
        "cantidad": item["cantidad"],  

    }

def serializeProductoCarritoList (productoCarrito) -> list:
    return [serializeProductoCarrito (item) for item in productoCarrito]