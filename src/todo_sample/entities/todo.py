import uuid
from datetime import datetime

from pydantic import BaseModel, Field, validator


class Todo(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    title: str
    description: str
    done: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = None  # type: ignore  # value assigned by validator

    @validator("updated_at", pre=True, always=True)
    def default_updated_at(cls, v, values, **kwargs):
        """avoid any ms difference between created_at and updated_at"""
        return v or values["created_at"]
