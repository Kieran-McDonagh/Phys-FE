from fastapi import APIRouter, Query
from backend.controllers.nutrition_controller import NutritionController
from backend.models.nutrition_models.new_nutrition_model import NewNutrition

router = APIRouter()


@router.get("/nutrition", status_code=200)
async def get_all(user_id: str = Query(None), sort_by_date: bool = Query(True)):
    return await NutritionController.get_all(user_id, sort_by_date)

@router.post("/nutrition", status_code=201)
async def post_nutrition(nutrition: NewNutrition):
    return await NutritionController.post_nutrition(nutrition)
