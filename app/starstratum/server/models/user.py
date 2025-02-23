from typing import Annotated, Optional
from pydantic import BaseModel, Field


class UserRegister(BaseModel):
    name: Annotated[str, Field(title="name")]
    password: Annotated[str, Field(title="password")]


    class Config:
        populate_by_name = True

