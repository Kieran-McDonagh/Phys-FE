from backend.database.connection import MongoConnection
from backend.models.user_models.user import User as UserModel
from backend.services.user_service import UserService
from backend.services.security_service import SecurityService
from fastapi import HTTPException
from bson import ObjectId


user_collection = MongoConnection().get_collection("users")


class UserRepository:
    @staticmethod
    async def fetch_all_users(username=None):
        query = {}
        if username:
            query["username"] = username

        users_list = []
        cursor = user_collection.find(query)
        for document in cursor:
            users_list.append(UserModel(**document))
        if len(users_list) > 0:
            return users_list
        else:
            raise HTTPException(status_code=404, detail="Users not found")

    @staticmethod
    async def fetch_by_id(id):
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid id")

        user = user_collection.find_one({"_id": ObjectId(id)})

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        else:
            return UserModel(**user)

    @staticmethod
    async def fetch_by_username(username):
        user = user_collection.find_one({"username": username})
        if user:
            user_dict = dict(user)
            return UserModel(**user_dict)

    @staticmethod
    async def add_user(user):
        existing_user = user_collection.find_one(
            {"$or": [{"username": user.username}, {"email": user.email}]}
        )
        if existing_user:
            return {"message": "Username or email already exists"}

        hashed_password = SecurityService.get_password_hash(user.password)
        new_user = user.dict()
        new_user["hashed_password"] = hashed_password
        del new_user["password"]
        new_user["workouts"] = []
        new_user["nutrition"] = []
        new_user["friends"] = []
        new_user["disabled"] = False
        user_collection.insert_one(new_user)

        return {"message": "User registered successfully"}

    @staticmethod
    async def edit_user(id, update):
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid id")

        update_dict = dict(update)
        updated_user = user_collection.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": update_dict}, return_document=True
        )

        if updated_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        else:
            return UserModel(**updated_user)

    @staticmethod
    async def remove_user(id):
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid id")

        try:
            await UserService.remove_user_from_all_friends_lists(user_collection, id)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to remove deleted user from friends lists, {e}",
            )

        deleted_user = user_collection.find_one_and_delete({"_id": ObjectId(id)})

        if deleted_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        else:
            return UserModel(**deleted_user)
