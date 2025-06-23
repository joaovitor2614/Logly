import jwt
from fastapi import APIRouter, Request, Response, HTTPException, status
from ..models.user.user import UserCreate, UserCrendentials
from fastapi.encoders import jsonable_encoder
from ..utils.security import verify_password
from app.settings import APP_SETTINGS
from ..controllers.user import UserController
from ..core.token import JWTHandler
from datetime import timedelta


router = APIRouter()


@router.post("/register", response_description="Register user in Database", status_code=status.HTTP_201_CREATED)
def register_user(request: Request, userInfo: UserCreate):
    user_controller = UserController(request)
    jwt_handler = JWTHandler()

    created_new_user = user_controller.create_user(userInfo)

    jwt_token = jwt_handler.get_jwt_token_from_user_db_obj(created_new_user)


    return {"token": jwt_token}


@router.post("/login", response_description="Login user", status_code=status.HTTP_201_CREATED)    
def login_user(request: Request, userInfo: UserCrendentials):
    user_controller = UserController(request)
    jwt_handler = JWTHandler()

  
    database =  request.app.database[APP_SETTINGS.USERS_DB_NAME]
    user = database.find_one(
        {"email": userInfo.email}    
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with given name does not exist"
        )

    user_controller.verify_password(userInfo.password, user["password"])

    jwt_token = jwt_handler.get_jwt_token_from_user_db_obj(user)



    return {"token": jwt_token}
  