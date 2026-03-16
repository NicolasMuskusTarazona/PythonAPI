from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "codegeasssecret"
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: int = 60*60):  # 1 hora
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(seconds=expires_delta)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token