from backend.services.nutrition_service import NutritionService
import pytest


def test_calculate_total_calories():
    test_dict = {"body": {"foo": 1, "bar": 2}}

    NutritionService.calculate_total_calories(test_dict)

    assert test_dict["total_calories"] == 3


def test_calculate_total_calories_exception():
    test_dict = {"body": {"foo": "banana", "bar": 2}}

    with pytest.raises(ValueError) as exc_info:
        NutritionService.calculate_total_calories(test_dict)

    assert (
        str(exc_info.value)
        == "Invalid input: values in 'body' dictionary must be convertible to integers"
    )
