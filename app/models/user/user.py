from typing import Annotated, Optional
from pydantic import BaseModel, Field, ConfigDict
from app.models import Base


class UserCrendentials(BaseModel):
    password: Annotated[str, Field(title="User Password")] 
    email: Annotated[str, Field(title="User Email Address")] 



     
    ConfigDict.extra = "allow"
    ConfigDict.populate_by_name = True

    
class UserCreate(Base, UserCrendentials):
    name: Annotated[str, Field(title="User Name")] 
    verification_code: Annotated[str, Field(title="User Email Verification Code")] = None
    image: Annotated[str | None, Field(title="User Profile Picture")] = ''
    has_confirmed_email: Annotated[bool, Field(title="Has user confirmed email address")] = False

     
    ConfigDict.extra = "allow"
    ConfigDict.populate_by_name = True

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    password: Optional[str] = Field(None)
    image: Annotated[Optional[str], Field(title="User Profile Picture")] = None
    