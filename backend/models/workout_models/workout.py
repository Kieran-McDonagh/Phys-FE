from pydantic import BaseModel
from datetime import datetime


class Workout(BaseModel):
    id: str
    type: str
    title: str
    body: dict
    author_id: str
    date_created: datetime

    def __init__(self, **data):
        if data.get("id"):
            data["id"] = str(data["id"])
        super().__init__(**data)
