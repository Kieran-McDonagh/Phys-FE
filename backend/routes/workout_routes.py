from fastapi import APIRouter, Query
from backend.controllers.workout_controller import WorkoutController
from backend.models.workout_models.new_workout import NewWorkout

router = APIRouter()


@router.get("/workouts", status_code=200)
async def get_all_workouts(
    author_id: str = Query(None), sort_by_date_created: bool = Query(True)
):
    return await WorkoutController.get_all_workouts(author_id, sort_by_date_created)


@router.get("/workouts/{id}", status_code=200)
async def get_workout_by_id(id: str):
    return await WorkoutController.get_by_id(id)


@router.post("/workouts", status_code=201)
async def post_workout(workout: NewWorkout):
    return await WorkoutController.post_workout(workout)


@router.put("/workouts/{id}", status_code=201)
async def update_workout_by_id(id: str, updated_workout: NewWorkout):
    return await WorkoutController.update_workout(id, updated_workout)


@router.delete("/workouts/{id}", status_code=200)
async def delete_workout_by_id(id: str):
    return await WorkoutController.delete_workout(id)
