from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from ..models.user import User
from dotenv import dotenv_values
import bcrypt

config = dotenv_values("../.env")

router = APIRouter()


@router.post("/register", response_description="Register user in Database", status_code=status.HTTP_201_CREATED)
def register_user(request: Request, userInfo: User):
    database =  request.app.database[config["DB_NAME"]]
    #userInfo = jsonable_encoder(userInfo)

    #user = database.find_one(
    #    {"name": userInfo.name}
    #)
    #if use:
    #    print('User with given name already exists!')
    #    return

    salt = bcrypt.gensalt()
    bytes_password = userInfo.password.encode('utf-8')
    hash_password = bcrypt.hashpw(
        password=bytes_password,
        salt=salt
    )
    user_password = bytes_password.decode('utf-8')



    userInfo.password = hash_password
    userInfo = jsonable_encoder(userInfo)
    created_user = database.insert_one(userInfo)
    return created_user
