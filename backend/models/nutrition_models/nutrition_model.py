from pydantic import BaseModel
from datetime import datetime


class NutritionModel(BaseModel):
    id: str
    date: datetime
    fat: int
    carbs: int
    protein: int
    body: dict
    user_id: str
    total_calories: int

    def __init__(self, **data):
        if data.get('_id'):
            data['id'] = str(data['_id'])
        super().__init__(**data)

    def calculate_total_calories(self) -> int:
        return sum(self.body.values())

    def __setattr__(self, key, value):
        if key == "body":
            object.__setattr__(self, "total_calories", sum(value.values()))
        return super().__setattr__(key, value)
