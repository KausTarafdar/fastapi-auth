from fastapi import FastAPI, APIRouter

from db.models import NewUser
from db.db import user_collection
from core.bcrypt_functions import hash_password
from utils.response_helpers import success_response, error_response

app = FastAPI()
router = APIRouter()

'''To create a new user with the role permissions'''
@router.post("/user/")
async def create_user(user: NewUser):
    # check if username exists
    valid_email = user_collection.find_one({"email": user.email})
    if valid_email:
        error_response(
            error_type="Conflict",
            details="User Creation Error",
            message="Email already exists",
            code=409
        )
    # generate a password hash
    hashed_password = hash_password(user.password)
    # enter user into users db
    user_collection.insert_one({
        "name": user.name,
        "password": hashed_password,
        "email": user.email,
        "role": user.role
    })
    # return credentials and status
    return success_response(
        data={
            "name": user.name,
            "email": user.email,
            "role": user.role
        },
        message="User Successfully Created",
        code=201
    )