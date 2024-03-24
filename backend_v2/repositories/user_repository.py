from backend_v2.database.connection import MongoConnection
from backend_v2.models.user_models.user import User as UserModel
from fastapi import HTTPException
from bson import ObjectId

mongo_connection = MongoConnection()
user_collection = mongo_connection.get_collection("users")


class UserRepository:
    @staticmethod
    async def fetch_all_users():
        users_list = []
        cursor = user_collection.find({})
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
    async def add_user(user):
        user_dict = dict(user)
        new_user = user_collection.insert_one(user_dict)
        inserted_id = new_user.inserted_id
        return UserModel(**{**user_dict, "_id": inserted_id})

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

        deleted_user = user_collection.find_one_and_delete({"_id": ObjectId(id)})

        if deleted_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        else:
            return UserModel(**deleted_user)
