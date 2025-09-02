
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class JWTPayload(BaseModel):
    data: dict
    iat: datetime
    exp: datetime

    ConfigDict.populate_by_name = True
  
