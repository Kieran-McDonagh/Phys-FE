from pydantic import BaseModel, Field
from datetime import datetime

class Workout(BaseModel):
    id: str = Field(alias="_id")
    type: str
    title: str
    body: dict
    author_id: str
    date_created: datetime
    
    def __init__(self, **data):
        if data.get('_id'):
            data['_id'] = str(data['_id'])
        super().__init__(**data)