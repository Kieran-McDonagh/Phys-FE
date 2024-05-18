from pydantic import BaseModel, field_validator
from bson import ObjectId


class NewWorkout(BaseModel):
    type: str
    title: str
    body: dict

    @field_validator("type")
    def validate_type(cls, v):
        valid_types = ("individual", "battlephys")
        if v not in valid_types:
            raise ValueError(f"type must be one of {valid_types}")
        return v
