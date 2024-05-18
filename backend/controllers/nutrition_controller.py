from backend.repositories.nutrition_repository import NutritionRepository


class NutritionController:
    @staticmethod
    async def get_all(user_id=None, sort_by_date=True):
        response = await NutritionRepository.fetch_all(user_id, sort_by_date)
        return response

    @staticmethod
    async def get_by_id(id):
        response = await NutritionRepository.fetch_by_id(id)
        return response

    @staticmethod
    async def post_nutrition(nutrition, current_user):
        response = await NutritionRepository.add_nutrition(nutrition, current_user)
        return response

    @staticmethod
    async def update_nutrition(id, update, current_user):
        response = await NutritionRepository.edit_nutrition(id, update, current_user)
        return response

    @staticmethod
    async def delete_nutrition(id, current_user):
        response = await NutritionRepository.remove_nutrition(id, current_user)
        return response
