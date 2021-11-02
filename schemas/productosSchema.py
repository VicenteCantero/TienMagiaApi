def serializeProducto(item) -> dict:

    return {
        "id": str (item["_id"]),
        "nombre": item["nombre"],
        "precio":item["precio"],
        "tipo":item["tipo"],
        "creador":item["creador"],
        "descripcion":item["descripcion"],
        "alt_img": item["alt_img"],
        "cantidad": item["cantidad"],
        

    }

def serializeProductoList (productos) -> list:
    return [serializeProducto (item) for item in productos]