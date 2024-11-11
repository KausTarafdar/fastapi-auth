from pydantic import BaseModel
from enum import Enum

class RolesEnum(str, Enum):
    ADMIN = 'ADMIN'
    USER = 'USER'

class UserInfo(BaseModel):
    email: str
    password: str

class NewUser(BaseModel):
    name: str
    email: str
    password: str
    role: RolesEnum