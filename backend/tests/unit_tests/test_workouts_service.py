from unittest.mock import patch
from datetime import datetime
from backend.services.workouts_service import WorkoutService


def test_apply_timestamp_to_new_workout():
    test_dict = {"foo": "bar"}
    fixed_datetime = datetime(2024, 4, 29, 12, 0, 0)

    with patch("backend.services.workouts_service.datetime") as mocked_datetime:
        mocked_datetime.now.return_value = fixed_datetime

        WorkoutService.apply_timestamp_to_new_workout(test_dict)

    assert test_dict["date_created"] == fixed_datetime


def test_apply_timestamp_to_new_workout_exception(capsys):
    test_dict = {"foo": "bar"}

    with patch("backend.services.workouts_service.datetime") as mocked_datetime:
        mocked_datetime.now.side_effect = Exception("Datetime error")

        WorkoutService.apply_timestamp_to_new_workout(test_dict)

    assert "date_created" not in test_dict
    assert (
        "An error occurred while applying timestamp to workout: Datetime error"
        in capsys.readouterr().out
    )
