from typing import Annotated, Optional
from pydantic import BaseModel, Field
import uuid

class UserCrendentials(BaseModel):
    password: Annotated[str, Field(title="User Password")] 
    email: Annotated[str, Field(title="User Email Address")] 



    class Config:
        populate_by_name = True

    
class UserCreate(UserCrendentials):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    email: Annotated[str, Field(title="User Email Address")] 
    name: Annotated[str, Field(title="User Name")] 
    image: Annotated[str | None, Field(title="User Profile Picture")] = ''
    has_confirmed_email: Annotated[bool, Field(title="Has user confirmed email address")] = False

    class Config:
        populate_by_name = True

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    password: Optional[str] = Field(None)
    image: Annotated[Optional[str], Field(title="User Profile Picture")] = None
    