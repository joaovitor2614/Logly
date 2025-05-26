import jwt
from fastapi import APIRouter, Request, Response, HTTPException, status
from ..models.user.user import UserCreate, UserCrendentials
from fastapi.encoders import jsonable_encoder
from ..utils.security import get_hashed_password, verify_password, encode_jwt_token, generate_jwt_token_payload_from_user_info
from app.settings import APP_SETTINGS
from ..controllers.user import UserController
from ..controllers.token import JWTController
from datetime import timedelta


router = APIRouter()


@router.post("/register", response_description="Register user in Database", status_code=status.HTTP_201_CREATED)
def register_user(request: Request, userInfo: UserCreate):
    user_controller = UserController(request)
    jwt_controller = JWTController()

    created_new_user = user_controller.create_user(userInfo)

    jwt_token = jwt_controller.get_jwt_token_from_user_db_obj(created_new_user)


    return {"token": jwt_token}


@router.post("/login", response_description="Login user", status_code=status.HTTP_201_CREATED)    
def login_user(request: Request, userInfo: UserCrendentials):
    user_controller = UserController(request)
    
    print('userInfo', userInfo)
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
    jwt_payload = generate_jwt_token_payload_from_user_info(user)
    jwt_payload.exp += timedelta(minutes=APP_SETTINGS.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    jwt_token = encode_jwt_token(jwt_payload)

    return {"token": jwt_token}
  