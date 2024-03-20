from backend.database.connection import MongoConnection
from bson import ObjectId
from backend.models.user_models.user import User as UserModel
import bson
from fastapi import HTTPException

mongo_connection = MongoConnection()
user_collection = mongo_connection.get_collection('users')

class User:
    @staticmethod
    async def create_user(user):
        result = await user_collection.insert_one(user)
        inserted_id = result.inserted_id
        return UserModel(**{**user, '_id': inserted_id})
    
    
    @staticmethod
    async def fetch_all_users():
        users = []
        cursor = user_collection.find({})
        async for document in cursor:
            users.append(UserModel(**document))
        if len(users) > 0:
            return users
        else: 
            raise HTTPException(status_code=404, detail="Users not found")
        
        
    @staticmethod
    async def fetch_user_by_id(id):
        try:
            user = await user_collection.find_one({"_id": ObjectId(id)})
            if user:
                return UserModel(**user)
            else:
                raise HTTPException(status_code=404, detail="User not found")
        except bson.errors.InvalidId:
            raise HTTPException(status_code=400, detail="Invalid ID")
        
    
    @staticmethod
    async def edit_user(id, user_update):
        try:
            updated_user = await user_collection.find_one_and_update({"_id": ObjectId(id)},
                                                                     {"$set": user_update},return_document=True)
            if updated_user:
                return UserModel(**updated_user)
            else:
                raise HTTPException(status_code=404, detail="user not found")
        except bson.errors.InvalidId:
            raise HTTPException(status_code=400, detail="invalid ID")
        
    
    @staticmethod
    async def remove_user(id):
        try:
            deleted_user = await user_collection.find_one_and_delete({"_id": ObjectId(id)})
            if deleted_user:
                return UserModel(**deleted_user)
            else:
                raise HTTPException(status_code=404, detail="user not found")
        except bson.errors.InvalidId:
            raise HTTPException(status_code=400, detail="invalid ID")