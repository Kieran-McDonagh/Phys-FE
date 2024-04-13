from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: str
    name: str
    email: EmailStr
    workouts: list
    friends: list
    
    def __init__(self, **data):
        if data.get('id'):
            data['id'] = str(data['id'])
        super().__init__(**data)