def serializeUsuarioDevuelto(item) -> dict:

    return {
        "id": str (item["_id"]),
        "nombre": item["nombre"],
        "email": item["email"]
    
    }

def serializeUsuarioDevueltoList (usuariosDevueltos) -> list:
    return [serializeUsuarioDevuelto (item) for item in usuariosDevueltos]