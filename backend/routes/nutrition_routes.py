from fastapi import APIRouter, Query
from backend.controllers.nutrition_controller import NutritionController
from datetime import datetime

router = APIRouter()


@router.get("/nutrition", status_code=200)
async def get_all(user_id: str = Query(None), sort_by_date: bool = Query(True)):
    return await NutritionController.get_all(user_id)
