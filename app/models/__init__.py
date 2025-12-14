

from pydantic import BaseModel, Field
from datetime import datetime
import uuid


def time_factory():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


class Base(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")