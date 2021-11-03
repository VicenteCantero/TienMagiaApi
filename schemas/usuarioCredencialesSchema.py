def serializeUsuarioCredenciales(item) -> dict:

    return {
        "id": str (item["_id"]),
        "nombre": item["nombre"],
        "password": item["password"]
    
    }

def serializeUsuarioCredencialesList (usuariosCredenciales) -> list:
    return [serializeUsuarioCredenciales (item) for item in usuariosCredenciales]