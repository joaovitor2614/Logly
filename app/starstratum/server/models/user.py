from typing import Annotated, Optional
from pydantic import BaseModel, Field
import uuid

class UserCrendentials(BaseModel):
    email: str = Field(...)
    password: str = Field(...)



    class Config:
        populate_by_name = True

    
class UserCreate(BaseModel):
    name: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)



    class Config:
        populate_by_name = True

    