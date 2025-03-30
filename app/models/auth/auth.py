
from pydantic import BaseModel
from datetime import datetime

class JWTPayload(BaseModel):
    data: dict
    iat: datetime
    exp: datetime

    # aud: str
    # iss: str
    # sub: str

    class Config:
        allow_extra = True
        populate_by_name = True
