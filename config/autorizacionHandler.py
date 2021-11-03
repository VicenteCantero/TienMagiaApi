
import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta


class AutorizacionHandler ():
    seguridad = HTTPBearer()
    passwordContext = CryptContext(schemes= ["bcrypt"], deprecated="auto")
    secreto = "Adrian"
    
    def encriptarPassword (self, password):
        return self.passwordContext.hash(password)

    def verificarPassword (self, password , hashPassword):
        return self.passwordContext.verify(password, hashPassword)

    def codificarToken (self, user_id):
        payload= {
            "expiracion": datetime.utcnow()+timedelta(days= 0 , minutes= 5),
            "user_id": user_id
        }

        return  jwt.encode (payload, self.secreto, algorithm='HS256')

    def decodificarToken (self, token):

        try:
            payload = jwt.decode (token, self.secreto, algorithm='HS256')
            return payload["user_id"]
        except jwt.ExpiredSignatureError:
            raise HTTPException (status_code= 401, detail="Tiempo expirado")
        except jwt.InvalidTokenError:
            raise HTTPException (status_code=401, detail="Token inválido")

    def authWrapper (self, auth: HTTPAuthorizationCredentials = Security(seguridad)):
        return self.decodificarToken(auth.credentials)
