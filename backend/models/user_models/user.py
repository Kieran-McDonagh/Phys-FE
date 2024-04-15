from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: str
    name: str
    email: EmailStr
    workouts: list
    friends: list
    
    def __init__(self, **data):
        if data.get('_id'):
            data['id'] = str(data['_id'])
        super().__init__(**data)