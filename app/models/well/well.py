from typing import Annotated, Optional, List, Literal
from pydantic import BaseModel, Field
from datetime import datetime
import uuid


class ImportWell(BaseModel):
    file_path: Annotated[str, Field(title="Well LAS file path", default="")] = ""
    well_name: Annotated[str, Field(title="Well name", default="")]

class WellLog(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    
    mnemonic: Annotated[str, Field(title="WellLog mnemonic", default="")]
    unit: Annotated[str, Field(title="WellLog unit", default="")]
    description: Annotated[str, Field(title="WellLog description", default="")]


class WellLogData(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    well_log_id: str = Field(default_factory=uuid.uuid4)
    well_id: str = Field(default_factory=uuid.uuid4)
    data: Annotated[List[float], Field(default_factory=list)] = []  # Ensuring a list

class Well(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    name: str = Field(...)
    user_id: str = Field(default_factory=uuid.uuid4)
    create_time: Annotated[
        Optional[datetime], Field(description="Well imported time", default_factory=datetime.utcnow)
    ] = None


    welllogs: Annotated[List[WellLog], Field(default_factory=list)] = []  # Ensuring a list
