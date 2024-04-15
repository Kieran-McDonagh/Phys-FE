from backend.repositories.nutrition_repository import NutritionRepository


class NutritionController:
    @staticmethod
    async def get_all(user_id=None, sort_by_date=True):
        response = await NutritionRepository.fetch_all(user_id, sort_by_date)
        return response
