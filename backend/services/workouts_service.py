from datetime import datetime
from bson import ObjectId
from fastapi import HTTPException


class WorkoutService:
    @staticmethod
    def apply_timestamp_to_new_workout(workout_dict):
        try:
            workout_dict["date_created"] = datetime.now()
        except Exception as e:
            print(f"An error occurred while applying timestamp to workout: {e}")

    @staticmethod
    def apply_workout_id_to_user(collection, workout_id, user_id):
        try:
            updated_user = collection.find_one_and_update(
                {"_id": ObjectId(user_id)},
                {"$push": {"workouts": str(workout_id)}},
                return_document=True,
            )
            if updated_user is None:
                raise HTTPException(
                    status_code=404,
                    detail="User not found",
                )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to apply workout ID to user: {e}",
            )
