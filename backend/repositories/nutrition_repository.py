from backend.database.connection import MongoConnection
from backend.models.nutrition_models.nutrition_model import NutritionModel
from backend.services.nutrition_service import NutritionService
from fastapi import HTTPException
from bson import ObjectId
import pymongo


mongo_connection = MongoConnection()
nutrition_collection = mongo_connection.get_collection("nutrition")


class NutritionRepository:
    @staticmethod
    async def fetch_all(user_id=None, sort_by_date=True):
        query = {}
        if user_id:
            if not ObjectId.is_valid(user_id):
                raise HTTPException(status_code=400, detail="Invalid id")
            query["user_id"] = user_id

        nutrition_list = []
        cursor = nutrition_collection.find(query)

        cursor = (
            cursor.sort("date_created", pymongo.DESCENDING)
            if sort_by_date
            else cursor.sort("date_created", pymongo.ASCENDING)
        )

        for document in cursor:
            nutrition_list.append(NutritionModel(**document))
        if len(nutrition_list) > 0:
            return nutrition_list
        else:
            raise HTTPException(status_code=404, detail="Nutrition data not found")

    @staticmethod
    async def add_nutrition(nutrition):
        nutrition_dict = dict(nutrition)
        NutritionService.apply_timestamp_to_nutrition(nutrition_dict)
        new_nutrition = nutrition_collection.insert_one(nutrition_dict)
        inserted_id = new_nutrition.inserted_id
        NutritionService.calculate_total_calories(nutrition_dict)
        return NutritionModel(**{**nutrition_dict, "id": inserted_id})
