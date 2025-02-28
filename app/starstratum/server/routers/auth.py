import jwt
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from ..models.user import UserCreate, UserCrendentials
from fastapi.encoders import jsonable_encoder
from dotenv import load_dotenv
from ..utils.security import get_hashed_password, verify_password

import os

config = load_dotenv()

DB_NAME = os.getenv("DB_NAME")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")


router = APIRouter()


@router.post("/register", response_description="Register user in Database", status_code=status.HTTP_201_CREATED)
def register_user(request: Request, userInfo: UserCreate):
    database =  request.app.database[DB_NAME]

    user = database.find_one(
        {"email": userInfo.email}
    )
    if user:
        print('User with given email already exists!')
        return 

 
   
    hashed_password = get_hashed_password(userInfo.password)
    userInfo.password = hashed_password

    userInfo = jsonable_encoder(userInfo)
    new_user = database.insert_one(userInfo)
    created_new_user = database.find_one(
        {"_id": new_user.inserted_id}
    )
    if created_new_user:
        # Convert `_id` from ObjectId to string
        created_new_user["_id"] = str(created_new_user["_id"])

    return created_new_user


@router.post("/login", response_description="Login user", status_code=status.HTTP_201_CREATED)    
def login_user(request: Request, userInfo: UserCrendentials):
    database =  request.app.database[DB_NAME]
    user = database.find_one(
        {"email": userInfo.email}    
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with given name does not exist!"
        )
    
    is_password_valid = verify_password(userInfo.password, user["password"])

    if not is_password_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Password is not valid!"
        )
    
    jwt_payload = {
        "name": user["name"],
        "email": user["email"],
        "id": str(user["_id"]),
        
    }
    jwt_token = jwt.encode(jwt_payload, SECRET_KEY, algorithm=JWT_ALGORITHM)
    print('jwt_token', jwt_token, type(jwt_token))
    return {"token": jwt_token}
  