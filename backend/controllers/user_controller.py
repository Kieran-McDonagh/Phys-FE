from fastapi import HTTPException
from repositories.user_repository import User

class UserController:
    @staticmethod
    async def post_user(user):
        response = await User.create_user(user.dict())
        return 201, {"New User": response}
    
    @staticmethod
    async def get_all_users():
        response = await User.fetch_all_users()
        return 200, {"all users": response}
        
    @staticmethod
    async def get_user_by_id(id: str):
        response = await User.fetch_user_by_id(id)
        return 200, {"user": response}

    @staticmethod
    async def update_user_by_id(id, user_update):
        result = await User.edit_user(id, user_update)
        return 201, {"updated user": result}
        
    @staticmethod
    async def delete_user_by_id(id):
        result = await User.remove_user(id)
        return 200, {"deleted user": result}