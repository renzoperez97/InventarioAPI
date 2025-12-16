import jwt
from datetime import datetime, timedelta

SECRET_KEY = "super_secret_key_123"
ALGORITHM = "HS256"
TOKEN_DURATION_MINUTES = 60

def crear_token(data: dict):

    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_DURATION_MINUTES)
    to_encode.update({"exp": expire})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token