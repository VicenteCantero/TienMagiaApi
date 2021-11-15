def serializeCarrito(item) -> dict:

    return {
        "id": str (item["_id"]),
        "usu_id": item ["usu_id"],
        #"fecha": item ["fecha"],
        "productoCarrito": item ["productoCarrito"],
        "total": item ["total"]
    
    }

def serializeCarritoList (carrito) -> list:
    return [serializeCarrito (item) for item in carrito]