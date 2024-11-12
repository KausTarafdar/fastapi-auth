from typing import Annotated

from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer

from ..db.models import NewUser, RolesEnum
from ..db.db import user_collection
from ..core.bcrypt_functions import hash_password
from ..core.token import get_user_from_token
from ..utils.response_helpers import success_response, error_response

router = APIRouter(
    prefix='/user',
    tags=['User']
)

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

'''To create a new user with the role permissions'''
@router.post("/new/")
async def create_user(user: NewUser, token: Annotated[str, Depends(oauth2_schema)]):
    verify_role = get_user_from_token(token)
    if not verify_role or verify_role['role'] != RolesEnum.ADMIN:
        return error_response(
            error_type="Forbidden",
            details="Permissions or User authorized",
            message="This action required privileged role",
            code=403
        )


    valid_email = user_collection.find_one({"email": user.email})
    if valid_email:
        return error_response(
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