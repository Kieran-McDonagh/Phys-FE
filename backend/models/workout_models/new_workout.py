from pydantic import BaseModel, field_validator
from bson import ObjectId


class NewWorkout(BaseModel):
    type: str
    title: str
    body: dict
    user_id: str

    @field_validator("type")
    def validate_type(cls, v):
        valid_types = {"individual", "battlephys"}
        if v not in valid_types:
            raise ValueError(f"type must be one of {valid_types}")
        return v

    @field_validator("user_id")
    def validate_user_id(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("user_id must be a valid MongoDB ObjectId")
        return str(v)
