from pydantic import BaseModel, field_validator
from bson import ObjectId


class NewNutrition(BaseModel):
    fat: int
    carbs: int
    protein: int
    body: dict
    user_id: str

    @field_validator("user_id")
    def validate_user_id(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("user_id must be a valid MongoDB ObjectId")
        return str(v)
