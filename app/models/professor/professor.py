from typing import Annotated, Optional, List
from pydantic import BaseModel, Field
from datetime import datetime
import uuid


class Comment(BaseModel):
    text: str = Field(...)
    author: str = Field(...)
    create_time: Annotated[datetime | None, Field(description="Comment added time", default_factory=datetime.utcnow)] = None



    class Config:
        populate_by_name = True


class UpVote(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user_id: str = Field(lias="_id")

class DownVote(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user_id: str = Field(lias="_id")

    
class Professor(BaseModel):
    name: str = Field(...)
    image: str = Field(...)
    phone: Annotated[str | None, Field(...)] = str
    comments: Annotated[List[str] | None, Field(...)] = []
    comments: Annotated[List[Comment] | None, Field(...)] = []
    create_time: Annotated[datetime | None, Field(description="Professor added time", default_factory=datetime.utcnow)] = None
    comments: Annotated[List[str], Field(title="Professor comments")] = ['']
    upvotes: Annotated[int | None, Field(...)] = int
    downvotes: Annotated[int | None, Field(...)] = int



