import jwt
import time


secreto = "123456"
ts= int(time.time())

token= jwt.encode(
    {'id':'1','nombre':'vicente', 'time':ts    },
    secreto,
    algorithm='HS256'
)

resuelto=jwt.decode(token, secreto, algorithms= ['HS256'])
print("-----token-------")
print(token)
print("------resuelto------")
print(resuelto)

