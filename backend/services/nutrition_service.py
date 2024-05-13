class NutritionService:
    @staticmethod
    def calculate_total_calories(nutrition_dict):
        try:
            nutrition_dict["body"] = {
                key: int(value) for key, value in nutrition_dict["body"].items()
            }
        except ValueError:
            raise ValueError(
                "Invalid input: values in 'body' dictionary must be convertible to integers"
            )
        total_calories = sum(nutrition_dict["body"].values())
        nutrition_dict["total_calories"] = total_calories
