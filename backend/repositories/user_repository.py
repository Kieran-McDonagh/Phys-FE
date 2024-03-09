from connection import user_collection
from bson import ObjectId
from models.user_models.user import User as UserModel

class User:
    @staticmethod
    async def create_user(user):
        result = await user_collection.insert_one(user)
        created_user = await user_collection.find_one({"_id": result.inserted_id})
        return UserModel(**created_user)

    @staticmethod
    async def fetch_all_users():
        users = []
        cursor = user_collection.find({})
        async for document in cursor:
            users.append(UserModel(**document))
        return users
    
    @staticmethod
    async def fetch_user_by_id(id):
        user = await user_collection.find_one({"_id": ObjectId(id)})
        return UserModel(**user)
    
    @staticmethod
    async def edit_user(id, user_update):
        update_query = {"$set": user_update}
        await user_collection.update_one({"_id": ObjectId(id)}, update_query)
        updated_user = await user_collection.find_one({"_id": ObjectId(id)})
        return UserModel(**updated_user)
    
    @staticmethod
    async def remove_user(id):
        deleted_user = await user_collection.find_one_and_delete({"_id": ObjectId(id)})
        if deleted_user:
            return UserModel(**deleted_user)
        else:
            return None