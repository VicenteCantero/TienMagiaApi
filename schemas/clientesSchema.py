def serializeCliente(item) -> dict:

    return {
        "id": str (item["_id"]),
        "nombre": item["nombre"],
        "email": item["email"],
        "password": item["password"]
    }

def serializeClienteList (clientes) -> list:
    return [serializeCliente (item) for item in clientes]