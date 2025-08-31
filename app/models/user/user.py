from typing import Annotated, Optional
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from app.models import Base
import uuid

class OTPCode(BaseModel):
    exp: datetime
    code: str
    user_id: str = Field(default_factory=uuid.uuid4)


class UserCrendentials(BaseModel):
    password: Annotated[str, Field(title="User Password")] 
    email: Annotated[str, Field(title="User Email Address")] 



     
    ConfigDict.extra = "allow"
    ConfigDict.populate_by_name = True

    
class UserCreate(Base, UserCrendentials):
    name: Annotated[str, Field(title="User Name")] 
    verification_code: Annotated[str, Field(title="User Email Verification Code")] = ""
    image: Annotated[str | None, Field(title="User Profile Picture")] = ''
    has_confirmed_email: Annotated[bool, Field(title="Has user confirmed email address")] = False
    reset_password_token: Annotated[str | None, Field(title="User Password Reset Token")] = None
    otp_code: Annotated[None | OTPCode, Field(title="User Account Verification OTP Code")] = None
     
    ConfigDict.extra = "allow"
    ConfigDict.populate_by_name = True
class UserResetPassword(Base):
    email: Annotated[str, Field(title="User Email Address")] 

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    password: Optional[str] = Field(None)
    image: Annotated[Optional[str], Field(title="User Profile Picture")] = None
    