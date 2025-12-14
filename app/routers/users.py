
from fastapi import APIRouter, Body, Request, HTTPException, status, Depends
from ..models.user.user import UserCreate, UserUpdate, UserResetPassword
from ..utils.security import get_current_user
from ..utils.database.update import update_document_object_instance
from ..utils.otp import generate_otp_code
from ..utils.email_service import EmailSender
from app.core.handler.token import JWTHandler
from ..controllers.user import UserController
from bson.objectid import ObjectId
from app.settings import APP_SETTINGS


router = APIRouter()

@router.put("/{id}", response_description="Update a user", response_model=UserCreate)
def update_user(id: str, request: Request, user: UserUpdate = Body(...), user_id: ObjectId = Depends(get_current_user)):
    database =  request.app.database[APP_SETTINGS.USERS_DB_NAME]
    user_data = user.dict(exclude_unset=True)
    updated_user = update_document_object_instance(database, id, user_data)

    return updated_user


@router.get("/{id}", response_description="Get user info by id in Database", status_code=status.HTTP_200_OK)
async def get_user_by_id(id: str, request: Request, user_id: ObjectId = Depends(get_current_user)):
    user_controller = UserController(request)
    user = user_controller.get_user_by_id(id)

    return user
@router.delete("/", response_description="Delete current user account", status_code=status.HTTP_200_OK)
async def delete_current_user(request: Request, user_id: ObjectId = Depends(get_current_user)):
    user_controller = UserController(request)
    user_id = str(user_id)
    user_controller.delete_user_account(user_id)

    

@router.get("/", response_description="Get user info in Database", status_code=status.HTTP_200_OK)
async def get_user(request: Request, user_id: ObjectId = Depends(get_current_user)):
    user_controller = UserController(request)
    user = user_controller.get_user_by_id(user_id)
    
    return user


@router.post("/send-verification-code", response_description="Send verification code to user email")
def send_verification_code(request: Request, user_id: ObjectId = Depends(get_current_user)):
    user_controller = UserController(request)

    user = user_controller.get_user_by_id(user_id)
    if user["has_confirmed_email"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="User has already confirmed email address"
        )
        return user
    otp_code = generate_otp_code()
    user_controller.set_user_verification_code(user, otp_code)
    
    email_sender = EmailSender()
    email_sender.send_verification_email(user["email"], otp_code)
    return {"message": "Verification code sent successfully"}
 

_RESET_PASSWORD_JWT_EXP_TIME_MINUTES = 5


@router.post("/send-reset-password-link", response_description="Send reset password link to user email")
def send_reset_password_link(request: Request, payload: UserResetPassword):
    user_controller = UserController(request)

    user = user_controller.get_user_by_email(payload.email)
    jwt_handler = JWTHandler()
    reset_password_jwt = jwt_handler.get_jwt_token_from_user_db_obj(user, _RESET_PASSWORD_JWT_EXP_TIME_MINUTES)
    user_controller.update_user_field(user["_id"], "reset_password_token", reset_password_jwt)
    email_sender = EmailSender()
    email_sender.send_reset_password_email(user["email"], reset_password_jwt)

    return {"message": "Reset password link sent successfully"}
    #otp_code = generate_otp_code()
    #user_controller.set_user_verification_code(user, otp_code)
    
    #email_sender = EmailSender()
    #email_sender.send_verification_email(user["email"], otp_code)
    #return {"message": "Verification code sent successfully"}
 
@router.put("/verify-verification-code/{code}", response_description="Attempt to verify user account")
def verify_user(request: Request, code: str, user_id: ObjectId = Depends(get_current_user)):
    user_controller = UserController(request)
    user = user_controller.get_user_by_id(user_id)
    if user["has_confirmed_email"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="User has already confirmed email address"
        )
        return user
   
    user_controller.verify_verification_code(user, code)
