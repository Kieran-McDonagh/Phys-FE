from unittest.mock import patch
from datetime import datetime
from backend.services.nutrition_service import NutritionService
import pytest


def test_apply_timestamp_to_new_nutrition():
    test_dict = {"foo": "bar"}
    fixed_datetime = datetime(2024, 4, 29, 12, 0, 0)

    with patch("backend.services.nutrition_service.datetime") as mocked_datetime:
        mocked_datetime.now.return_value = fixed_datetime

        NutritionService.apply_timestamp_to_nutrition(test_dict)

    assert test_dict["date_created"] == fixed_datetime


def test_apply_timestamp_to_nutrition_exception(capsys):
    test_dict = {"foo": "bar"}

    with patch("backend.services.nutrition_service.datetime") as mocked_datetime:
        mocked_datetime.now.side_effect = Exception("Datetime error")

        NutritionService.apply_timestamp_to_nutrition(test_dict)

    assert "date_created" not in test_dict
    assert (
        "An error occurred while applying timestamp to nutrition: Datetime error"
        in capsys.readouterr().out
    )


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
