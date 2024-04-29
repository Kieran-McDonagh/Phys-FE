from datetime import datetime


class NutritionService:
    @staticmethod
    def apply_timestamp_to_nutrition(nutrition_dict):
        nutrition_dict["date_created"] = datetime.now()

    @staticmethod
    def calculate_total_calories(nutrition_dict):
        total_calories = sum(value for value in nutrition_dict["body"].values())
        nutrition_dict["total_calories"] = total_calories

        
        
