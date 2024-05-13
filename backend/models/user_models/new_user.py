from pydantic import BaseModel, EmailStr
    
class NewUser(BaseModel):
    email: EmailStr
    workouts: list = []
    nutrition: list = []
    friends: list = []
    username: str
    full_name: str
    disabled: bool = False
    password: str