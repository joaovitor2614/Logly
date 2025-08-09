

from pydantic import BaseModel, Field
import uuid


class Base(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")