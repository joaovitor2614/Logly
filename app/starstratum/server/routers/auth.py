from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from ..models.user import User
from dotenv import dotenv_values
import bcrypt

config = dotenv_values("../.env")

router = APIRouter()


@router.post("/register", response_description="Register user in Database", status_code=status.HTTP_201_CREATED)
def register_user(request: Request, userInfo: User):
    database =  request.app.database[config["DB_NAME"]]

    user = database.find_one(
        {"name": userInfo.name}
    )
    if user:
        print('User with given name already exists!')

    salt = bcrypt.gensalt()
    bytes_password = userInfo.password.encode('utf-8')
    hash_password = bcrypt.hashpw(
        password=bytes_password,
        salt=salt
    )
    user_passwrd = bytes_password.decode('utf-8')
    return {'actual_password': user_passwrd, 'hashed_password': hash_password}
