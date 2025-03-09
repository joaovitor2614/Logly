from typing import Annotated, Optional, List
from pydantic import BaseModel, Field
import uuid

class Professor(BaseModel):
    name: str = Field(...)
    image: str = Field(...)
    disciplines: List[str] = Field(...)
    upvotes: int =  Field(...)
    downvotes: int =  Field(...)


    class Config:
        populate_by_name = True

    
