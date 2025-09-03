
from fastapi import APIRouter, Request, HTTPException, status, Depends
from ..models.user.user import UserSendResetPassword, UserResetPassword
from ..utils.security import get_current_user, get_hashed_password
from ..utils.otp import generate_otp_code
from ..utils.email_service import EmailSender
from app.core.token import JWTHandler
from ..controllers.user import UserController
from bson.objectid import ObjectId


router = APIRouter()


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
def send_reset_password_link(request: Request, payload: UserSendResetPassword):
    user_controller = UserController(request)

    user = user_controller.get_user_by_email(payload.email)
    jwt_handler = JWTHandler()
    reset_password_jwt = jwt_handler.get_jwt_token_from_user_db_obj(user, _RESET_PASSWORD_JWT_EXP_TIME_MINUTES)
    user_controller.update_user_field(user["_id"], "reset_password_token", reset_password_jwt)
    email_sender = EmailSender()
    email_sender.send_reset_password_email(user["email"], reset_password_jwt)

    return {"message": "Reset password link sent successfully"}

@router.post("/reset-password-link/{token}", response_description="Reset passwordl")
def reset_password_link(request: Request, token: str, payload: UserResetPassword):
    jwt_handler = JWTHandler()
    try:
        jwt_payload = jwt_handler.decode_jwt_token(token)
 
        user_id = jwt_payload["data"].get("id", None)
        user_controller = UserController(request)
        hashed_password = get_hashed_password(payload.password)
        user_controller.update_user_field(user_id, "password", hashed_password)
        return {"message": "Password reset successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

   
 
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
