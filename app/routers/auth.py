import jwt
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from ..models.user import UserCreate, UserCrendentials
from fastapi.encoders import jsonable_encoder
from ..utils.security import get_hashed_password, verify_password, encode_jwt_token
from app.settings import APP_SETTINGS


router = APIRouter()


@router.post("/register", response_description="Register user in Database", status_code=status.HTTP_201_CREATED)
def register_user(request: Request, userInfo: UserCreate):
    database =  request.app.database[APP_SETTINGS.USERS_DB_NAME]

    user = database.find_one(
        {"email": userInfo.email}
    )
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User with given email already exists!"
        )
 
    hashed_password = get_hashed_password(userInfo.password)
    userInfo.password = hashed_password

    userInfo = jsonable_encoder(userInfo)
    new_user = database.insert_one(userInfo)
    created_new_user = database.find_one(
        {"_id": new_user.inserted_id}
    )

    jwt_token = encode_jwt_token(created_new_user["email"], created_new_user["_id"])

    return {"token": jwt_token}


@router.post("/login", response_description="Login user", status_code=status.HTTP_201_CREATED)    
def login_user(request: Request, userInfo: UserCrendentials):
    database =  request.app.database[APP_SETTINGS.USERS_DB_NAME]
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

    jwt_token = encode_jwt_token(user["email"], user["_id"])

    return {"token": jwt_token}
  