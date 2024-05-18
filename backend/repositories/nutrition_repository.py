from backend.database.connection import MongoConnection
from backend.models.nutrition_models.nutrition import Nutrition
from backend.services.nutrition_service import NutritionService
from backend.services.user_service import UserService
from backend.services.timestamp_service import TimestampService
from fastapi import HTTPException
from bson import ObjectId
import pymongo


mongo_connection = MongoConnection()
nutrition_collection = mongo_connection.get_collection("nutrition")
user_collection = mongo_connection.get_collection("users")


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
            nutrition_list.append(Nutrition(**document))
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
            return Nutrition(**data)

    @staticmethod
    async def add_nutrition(nutrition, current_user):
        nutrition_dict = dict(nutrition)
        nutrition_dict["user_id"] = current_user.id
        TimestampService.apply_timestamp_to_document(nutrition_dict)
        try:
            NutritionService.calculate_total_calories(nutrition_dict)
        except Exception as e:
            raise HTTPException(
                status_code=422, detail=f"Failed to calculate total calories, {e}"
            )

        new_nutrition = nutrition_collection.insert_one(nutrition_dict)
        inserted_id = new_nutrition.inserted_id

        try:
            UserService.apply_document_id_to_user(
                user_collection, inserted_id, current_user.id, "nutrition"
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to add nutrition data id to user, {e}",
            )

        return Nutrition(**{**nutrition_dict, "id": inserted_id})

    @staticmethod
    async def edit_nutrition(id, update, current_user):
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid id")
        if id not in current_user.nutrition:
            raise HTTPException(
                status_code=401, detail="Cannot edit other users nutrition data"
            )

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
            return Nutrition(**updated_nutrition)

    @staticmethod
    async def remove_nutrition(id, current_user):
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid id")
        if id not in current_user.nutrition:
            raise HTTPException(
                status_code=401, detail="Cannot delete other users nutrition data"
            )

        deleted_nutrition = nutrition_collection.find_one_and_delete(
            {"_id": ObjectId(id)}
        )

        if deleted_nutrition is None:
            raise HTTPException(status_code=404, detail="Nutrition data not found")
        else:
            try:
                UserService.remove_document_id_from_user(
                    user_collection, id, deleted_nutrition["user_id"], "nutrition"
                )
            except Exception as e:
                raise HTTPException(
                    status_code=500,
                    detail=f"Failed to remove nutrition data id from user, {e}",
                )
            return Nutrition(**deleted_nutrition)
