from fastapi import FastAPI, APIRouter
from db.models import UserInfo

app = FastAPI()
router = APIRouter()

'''Login to generate JWT for user session'''
@router.post("/login/")
async def login_user(user: UserInfo):
    # check for jwt not existing
    # validate password
    # set jwt
    # return logged in status
    pass

'''Logout route to expire user session'''
@router.get("/logout/")
async def logout_user():
    # validate jwt
    # expire jwt
    # return logged out status
    pass