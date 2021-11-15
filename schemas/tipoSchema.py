def serializeTipo(item) -> dict:

    return {
        "id": str (item["_id"]),
        "nombre": item ["nombre"],
       
    }

def serializeTipoList (tipo) -> list:
    return [serializeTipo (item) for item in tipo]