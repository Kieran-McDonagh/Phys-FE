from backend.repositories.workout_repository import WorkoutRepository


class WorkoutController:
    @staticmethod
    async def get_all_workouts(user_id=None, sort_by_date=True):
        workouts = await WorkoutRepository.fetch_all_workouts(
            user_id, sort_by_date
        )
        return workouts

    @staticmethod
    async def get_by_id(id):
        workout = await WorkoutRepository.fetch_by_id(id)
        return workout

    @staticmethod
    async def post_workout(workout, current_user):
        new_workout = await WorkoutRepository.add_workout(workout, current_user)
        return new_workout

    @staticmethod
    async def update_workout(id, update, current_user):
        updated_workout = await WorkoutRepository.edit_workout(id, update, current_user)
        return updated_workout

    @staticmethod
    async def delete_workout(id, current_user):
        deleted_workout = await WorkoutRepository.remove_workout(id, current_user)
        return deleted_workout
