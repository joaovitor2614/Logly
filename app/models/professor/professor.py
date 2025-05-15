from typing import Annotated, Optional, List, Literal
from pydantic import BaseModel, Field
from datetime import datetime
import uuid

def formatted_datetime():
    current_date_and_hour = datetime.now()
    return current_date_and_hour.strftime('%d/%m/%Y %H:%M')



class Comment(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user_id: str = Annotated[datetime | None, Field(description="Comment user ID", default_factory='')]
    text: str = Field(...)

    create_time: Annotated[datetime | None, Field(description="Comment added time", default_factory=formatted_datetime)] = None



    class Config:
        populate_by_name = True


class UpVote(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user_id: str = Field(...)

class DownVote(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user_id: str = Field(...)

    
class Professor(BaseModel):
    name: str = Field(...)
    image: str = Field(...)
    phone: Annotated[Optional[str], Field(...)] = None  
    gender : Annotated[Literal["male", "female", "other"], Field(...)] = "other"
    comments: Annotated[List[Comment], Field(title="Professor comments")] = [] 
    disciplines: Annotated[List[str], Field(...)] = []  
    create_time: Annotated[
        Optional[datetime], Field(description="Professor added time", default_factory=datetime.utcnow)
    ] = None

    upvotes: Annotated[List[UpVote], Field(default_factory=list)] = []  # Ensuring a list
    downvotes: Annotated[List[DownVote], Field(default_factory=list)] = []  # Ensuring a list



