from backend.database.connection import MongoConnection
from backend.models.workout_models.workout import Workout as WorkoutModel
from backend.services.workouts_service import WorkoutService
from fastapi import HTTPException
from bson import ObjectId
import pymongo

mongo_connection = MongoConnection()
workout_collection = mongo_connection.get_collection("workouts")


class WorkoutRepository:
    @staticmethod
    async def fetch_all_workouts(user_id=None, sort_by_date=True):
        query = {}
        if user_id:
            if not ObjectId.is_valid(user_id):
                raise HTTPException(status_code=400, detail="Invalid id")
            query["user_id"] = user_id

        workouts_list = []
        cursor = workout_collection.find(query)

        if sort_by_date:
            cursor = cursor.sort("date_created", pymongo.DESCENDING)

        for document in cursor:
            workouts_list.append(WorkoutModel(**document))
        if len(workouts_list) > 0:
            return workouts_list
        else:
            raise HTTPException(status_code=404, detail="Workouts not found")

    @staticmethod
    async def fetch_by_id(id):
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid id")

        workout = workout_collection.find_one({"_id": ObjectId(id)})

        if workout is None:
            raise HTTPException(status_code=404, detail="workout not found")
        else:
            return WorkoutModel(**workout)

    @staticmethod
    async def add_workout(workout):
        workout_dict = dict(workout)
        WorkoutService.apply_timestamp_to_new_workout(workout_dict)
        new_workout = workout_collection.insert_one(workout_dict)
        inserted_id = new_workout.inserted_id
        return WorkoutModel(**{**workout_dict, "id": inserted_id})

    @staticmethod
    async def edit_workout(id, update):
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid id")

        update_dict = dict(update)
        updated_workout = workout_collection.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": update_dict}, return_document=True
        )

        if updated_workout is None:
            raise HTTPException(status_code=404, detail="Workout not found")
        else:
            return WorkoutModel(**updated_workout)

    @staticmethod
    async def remove_workout(id):
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid id")

        deleted_workout = workout_collection.find_one_and_delete({"_id": ObjectId(id)})

        if deleted_workout is None:
            raise HTTPException(status_code=404, detail="Workout not found")
        else:
            return WorkoutModel(**deleted_workout)
