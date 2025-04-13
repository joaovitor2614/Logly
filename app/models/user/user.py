from typing import Annotated, Optional
from pydantic import BaseModel, Field
import uuid

class UserCrendentials(BaseModel):
    email: str = Field(...)
    password: str = Field(...)



    class Config:
        populate_by_name = True

    
class UserCreate(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    image: Annotated[str | None, Field(title="User Profile Picture")] = ''



    class Config:
        populate_by_name = True

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    password: Optional[str] = Field(None)
    image: Annotated[Optional[str], Field(title="User Profile Picture")] = None
    