import os
from fastapi import Depends, FastAPI, HTTPException, status
from datetime import datetime, timedelta
from jose import JWTError, jwt
from dotenv import load_dotenv
from pydantic import BaseModel

from ..db.models import UserInfo

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRES_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    name: str
    role: str

def generate_jwt_token(user: UserInfo) -> Token:
    return jwt.encode(
        {
            "name": user["name"],
            "role": user["role"],
            "exp": datetime.now() + timedelta(minutes=30)
        },
        SECRET_KEY,
        ALGORITHM
    )

def get_user_from_token(token: Token) -> TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        name: str = payload.get('name')
        role: str = payload.get('role')
        if name is None or role is None:
            return False
        return {
            'name': name,
            'role': role
        }
    except JWTError:
        return False