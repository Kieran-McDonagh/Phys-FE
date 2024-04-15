from backend.database.connection import MongoConnection
from backend.models.nutrition_models.nutrition_model import NutritionModel
from fastapi import HTTPException
import pymongo


mongo_connection = MongoConnection()
nutrition_collection = mongo_connection.get_collection("nutrition")


class NutritionRepository:
    @staticmethod
    async def fetch_all(user_id=None, sort_by_date=True):
        query = {}
        if user_id:
            query["user_id"] = user_id

        nutrition_list = []
        cursor = nutrition_collection.find(query)

        if sort_by_date:
            cursor = cursor.sort("date", pymongo.DESCENDING)

        for document in cursor:
            nutrition_list.append(NutritionModel(**document))
        if len(nutrition_list) > 0:
            return nutrition_list
        else:
            raise HTTPException(status_code=404, detail="Nutrition data not found")
