from typing import Annotated, Optional, List, Literal
from pydantic import BaseModel, Field
from datetime import datetime
import uuid


class WellLog(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user_id: str = Field(...)
    data = Annotated[List[float], Field(default_factory=list)] = []  # Ensuring a list

class Well(BaseModel):
    name: str = Field(...)

    create_time: Annotated[
        Optional[datetime], Field(description="Well imported time", default_factory=datetime.utcnow)
    ] = None
    user_id: str = Field(...)

    welllogs: Annotated[List[WellLog], Field(default_factory=list)] = []  # Ensuring a list
