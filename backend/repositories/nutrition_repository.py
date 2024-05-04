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
    async def fetch_by_id(id):
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid id")

        data = nutrition_collection.find_one({"_id": ObjectId(id)})

        if data is None:
            raise HTTPException(status_code=404, detail="Nutrition data not found")
        else:
            return NutritionModel(**data)

    @staticmethod
    async def add_nutrition(nutrition):
        nutrition_dict = dict(nutrition)
        NutritionService.apply_timestamp_to_nutrition(nutrition_dict)
        try:
            NutritionService.calculate_total_calories(nutrition_dict)
        except Exception as e:
            raise HTTPException(
                status_code=422, detail=f"Failed to calculate total calories, {e}"
            )
        new_nutrition = nutrition_collection.insert_one(nutrition_dict)
        inserted_id = new_nutrition.inserted_id

        return NutritionModel(**{**nutrition_dict, "id": inserted_id})

    @staticmethod
    async def edit_nutrition(id, update):
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid id")

        update_dict = dict(update)
        try:
            NutritionService.calculate_total_calories(update_dict)
        except Exception as e:
            raise HTTPException(
                status_code=422, detail=f"Failed to calculate total calories, {e}"
            )
        updated_nutrition = nutrition_collection.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": update_dict}, return_document=True
        )

        if updated_nutrition is None:
            raise HTTPException(status_code=404, detail="Nutrition data not found")
        else:
            return NutritionModel(**updated_nutrition)

    @staticmethod
    async def remove_nutrition(id):
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid id")

        deleted_nutrition = nutrition_collection.find_one_and_delete(
            {"_id": ObjectId(id)}
        )

        if deleted_nutrition is None:
            raise HTTPException(status_code=404, detail="Nutrition data not found")
        else:
            return NutritionModel(**deleted_nutrition)
