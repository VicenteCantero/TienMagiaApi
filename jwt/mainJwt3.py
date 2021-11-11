import jwt
import typing

secreto = "123456"

payload = {
    "id": "23"
}

def escribe_codigo (payload:dict):
    token_bytes = jwt.encode (payload, secreto, algorithm='HS256')
    return token_bytes

data= escribe_codigo(payload)

print(data)

def validar_token (encode_jwt):
    try:
        response = jwt.decode (encode_jwt, secreto, algorithms=['HS256'])
        return response
    except jwt.exceptions.DecodeError:
        return "Token no valido"

response_token= validar_token(data)

print(response_token)
