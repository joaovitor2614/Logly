import jwt
from fastapi import APIRouter, Request, Response, HTTPException, status
from ..models.user.user import UserCreate, UserCrendentials
from fastapi.encoders import jsonable_encoder
from app.settings import APP_SETTINGS
from ..utils.email_service import EmailSender

from datetime import timedelta


router = APIRouter()


@router.post("/", response_description="Generate code to verify user email", status_code=status.HTTP_201_CREATED)
def verify_user_acount(request: Request):
    email_sender = EmailSender()


    email_sender.send_verification_email("jvitoralvesestrella@gmail.com")