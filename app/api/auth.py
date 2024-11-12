from fastapi import FastAPI, APIRouter
from fastapi.security import OAuth2PasswordBearer

from ..db import models
from ..core.authenticate_user import authenticate_user
from ..core.token import generate_jwt_token
from ..utils.response_helpers import success_response, error_response

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

'''Login to generate JWT for user session'''
@router.post("/login/")
async def login_user(user: models.UserInfo):
    auth_user = authenticate_user(user)
    if not auth_user:
        return error_response(
            error_type="Unauthorized",
            details="Authentication Error",
            message="Email or Password is wrong",
            code=401
        )

    access_token = generate_jwt_token(user=auth_user)
    print(access_token)
    return success_response(
        data={
            'access_token': access_token,
            'token_type': 'bearer'
        },
        message="User Authenticated",
        code=202
    )


'''Logout route to expire user session'''
@router.get("/logout/")
async def logout_user():
    pass