from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from ..models.user import User
from fastapi.encoders import jsonable_encoder
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
    binary_hash_password = bcrypt.hashpw(
        password=bytes_password,
        salt=salt
    )
    str_hashed_password = binary_hash_password.decode('utf-8')
    userInfo.password = str_hashed_password
    userInfo = jsonable_encoder(userInfo)
    new_user = database.insert_one(userInfo)
    created_new_user = database.find_one(
        {"_id": new_user.inserted_id}
    )
    if created_new_user:
        # Convert `_id` from ObjectId to string
        created_new_user["_id"] = str(created_new_user["_id"])

    return created_new_user

