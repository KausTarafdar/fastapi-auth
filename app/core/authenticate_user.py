from typing import Union

from ..db import models, db
from .bcrypt_functions import verify_password

def authenticate_user(user: models.UserInfo) -> Union[bool, dict]:
    db_user = db.user_collection.find_one({'email': user.email})
    print(db_user)
    if db_user == None:
        return False
    verified = verify_password(user.password, db_user['password'])

    return {
        "name": db_user['name'],
        "email": db_user['email'],
        "role": db_user['role']
    } if verified else False