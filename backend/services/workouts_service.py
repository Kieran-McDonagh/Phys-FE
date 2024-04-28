from datetime import datetime


class WorkoutService:
    @staticmethod
    def apply_timestamp_to_new_workout(workout_dict):
        workout_dict["date_created"] = datetime.now()
