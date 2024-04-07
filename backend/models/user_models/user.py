from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    id: str = Field(alias="_id")
    name: str
    email: EmailStr
    workouts: list
    friends: list
    
    def __init__(self, **data):
        if data.get('_id'):
            data['_id'] = str(data['_id'])
        super().__init__(**data)