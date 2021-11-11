def serializeUsuario(item) -> dict:

    return {
        "id": str (item["_id"]),
        "nombre": item["nombre"],
        "email": item["email"],
        "password": item["password"]
    }

def serializeUsuarioList (usuarios) -> list:
    return [serializeUsuario (item) for item in usuarios]