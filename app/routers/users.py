
from fastapi import APIRouter, Request, HTTPException, status, Depends
from ..models.user.user import UserSendResetPassword, UserResetPassword
from ..utils.security import get_current_user, get_hashed_password
from ..utils.otp import generate_otp_code
from ..utils.email_service import EmailSender
from app.core.handlers.token import JWTHandler
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
    user_controller.set_user_verification_code(user, otp_code, "account_verification")
    
    email_sender = EmailSender()
    email_sender.send_verification_email(user["email"], otp_code)
    return {"message": "Verification code sent successfully"}
 

_RESET_PASSWORD_JWT_EXP_TIME_MINUTES = 5


@router.post("/send-reset-password-code", response_description="Send reset password link to user email")
def send_reset_password_link(request: Request, payload: UserSendResetPassword):
    user_controller = UserController(request)

    user = user_controller.get_user_by_email(payload.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found!"
        )

    otp_code = generate_otp_code()
    user_controller.set_user_verification_code(user, otp_code, "reset_password")
    email_sender = EmailSender()
    email_sender.send_reset_password_email(user["email"], otp_code)


    return {"message": "Reset password link sent successfully"}
@router.post("/verify-reset-password-code")
def verify_reset_password_code(request: Request, payload: UserResetPassword):
    
    user_controller = UserController(request)
    user = user_controller.get_user_by_email(payload.email)

    otp_code_type = "reset_password"
    user_controller.verify_verification_code(user, payload.otp_code, otp_code_type)

@router.post("/reset-password", response_description="Reset password")
def reset_password_link(request: Request, payload: UserResetPassword):
    user_controller = UserController(request)
    user = user_controller.get_user_by_email(payload.email)
    otp_code_type = "reset_password"
    user_controller.verify_verification_code(user, payload.otp_code, otp_code_type)



    hashed_password = get_hashed_password(payload.password)
    user_controller.update_user_field(user["_id"], "password", hashed_password)
    return {"message": "Password reset successfully"}


   
 
@router.post("/verify-account-verification-code/{code}", response_description="Attempt to verify user account")
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
    user_controller.set_user_acccount_verified_status(user)
