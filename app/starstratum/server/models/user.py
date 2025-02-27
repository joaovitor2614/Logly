from typing import Annotated, Optional
from pydantic import BaseModel, Field
import uuid

class User(BaseModel):
    name: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)



    class Config:
        populate_by_name = True

    