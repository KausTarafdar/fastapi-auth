from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from .api import auth, user

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)