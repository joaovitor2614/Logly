from typing import Annotated, Optional
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from app.models import Base
import uuid

class OTPCode(BaseModel):
    exp: datetime | None = None
    code: str = ''
    user_id: str = ''


class UserCrendentials(BaseModel):
    password: Annotated[str, Field(title="User Password")] 
    email: Annotated[str, Field(title="User Email Address")] 


    ConfigDict.populate_by_name = True

    
class UserCreate(Base, UserCrendentials):
    name: Annotated[str, Field(title="User Name")] 
    verification_code: Annotated[str, Field(title="User Email Verification Code")] = ""
    image: Annotated[str | None, Field(title="User Profile Picture")] = ''
    has_confirmed_email: Annotated[bool, Field(title="Has user confirmed email address")] = False
    verify_account_otp_code: Annotated[OTPCode, Field(title="User Account Verification OTP Code")] = OTPCode()
    reset_password_otp_code: Annotated[OTPCode, Field(title="User Password Reset OTP Code")] = OTPCode()
     
    ConfigDict.populate_by_name = True


class UserSendResetPassword(Base):
    email: Annotated[str, Field(title="User Email Address")] 


class UserResetPassword(Base):
    password: Annotated[str, Field(title="User Password")] = ''
    otp_code: Annotated[str, Field(title="User Password Reset OTP Code")]
    email: Annotated[str, Field(title="User Email Address")] 
