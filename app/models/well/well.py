from typing import Annotated, Optional, List
from pydantic import BaseModel, Field
from app.models import Base, time_factory

import uuid


class ImportWell(BaseModel):
    file_path: Annotated[str, Field(title="Well LAS file path", default="")] = ""
    well_name: Annotated[str, Field(title="Well name", default="")]

class WellLog(Base):
    name: Annotated[str, Field(title="WellLog mnemonic", default="")]
    unit: Annotated[str, Field(title="WellLog unit", default="")]
    min_value: Annotated[float, Field(title="WellLog min", default=0.0)]
    max_value: Annotated[float, Field(title="WellLog max", default=0.0)]
    description: Annotated[str, Field(title="WellLog description", default="")]


class WellLogData(Base):
    well_log_id: str = Field(default_factory=uuid.uuid4)
    well_id: str = Field(default_factory=uuid.uuid4)
    data: Annotated[List[float], Field(default_factory=list)] = []  # Ensuring a list

class Well(Base):
    name: str = Field(...)
    user_id: str = Field(default_factory=uuid.uuid4)
    company: str = Field(...)
    start: float = Field(default=0.0)
    stop: float = Field(default=0.0)
    create_time: Annotated[
        Optional[str], Field(description="Well imported time", default_factory=time_factory)
    ] = None


    welllogs: Annotated[List[WellLog], Field(default_factory=list)] = []  # Ensuring a list

class WellCalculator(BaseModel):
    well_id: str = Field(default_factory=uuid.uuid4)
    formula: str = Field(description="Well calculation formula", default="")