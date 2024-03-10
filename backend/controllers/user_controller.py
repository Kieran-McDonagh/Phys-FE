from fastapi import HTTPException
from repositories.user_repository import User

class UserController:
    @staticmethod
    async def post_user(user):
        response = await User.create_user(user.dict())
        return 201, {"data": {"new_user": response}}
    
    
    @staticmethod
    async def get_all_users():
        try:
            users = await User.fetch_all_users()
            return 200, {"data": {"all_users": users}}
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal server error")
        
        
    @staticmethod
    async def get_user_by_id(id: str):
        try:
            response = await User.fetch_user_by_id(id)
            return 200, {"data": {"user": response}}
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal server error")
        
    
    @staticmethod
    async def update_user_by_id(id, user_update):
        try:
            response = await User.edit_user(id, user_update)
            return 201, {"data": {"updated_user": response}}
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal server error")


    @staticmethod
    async def remove_user(id):
        try:
            response = await User.remove_user(id)
            return 200, {"data": response}
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal server error")