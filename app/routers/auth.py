
from fastapi import APIRouter, Request, HTTPException, status
from ..models.user.user import UserCreate, UserCrendentials
from app.settings import APP_SETTINGS
from ..controllers.user import UserController
from ..core.token import jwt_handler



router = APIRouter()


@router.post("/register", response_description="Register user in Database", status_code=status.HTTP_201_CREATED)
def register_user(request: Request, userInfo: UserCreate):
    user_controller = UserController(request)
    created_new_user = user_controller.create_user(userInfo)

    jwt_token = jwt_handler.get_jwt_token_from_user_db_obj(created_new_user)


    return {"token": jwt_token}


@router.post("/login", response_description="Login user", status_code=status.HTTP_201_CREATED)    
def login_user(request: Request, userInfo: UserCrendentials):
    user_controller = UserController(request)


    user = user_controller.get_user_by_email(userInfo.email)

    user_controller.verify_password(userInfo.password, user["password"])

    jwt_token = jwt_handler.get_jwt_token_from_user_db_obj(user)



    return {"token": jwt_token}
  