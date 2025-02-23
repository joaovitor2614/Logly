from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from ..models.user import UserRegister
from dotenv import dotenv_values

config = dotenv_values(".env")

router = APIRouter()


@router.post("/register", response_description="Register user in Database", status_code=status.HTTP_201_CREATED)
def register_user(request: Request, userInfo: User):
    database =  request.app.database[config["DB_NAME"]]

    user = database.find_one(
        {"name": userInfo.name}
    )
    if user:
        print('User with given name already exists!')
