from unittest.mock import patch
import pytest
from datetime import datetime
from unittest.mock import MagicMock
from bson import ObjectId
from fastapi import HTTPException
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


def test_apply_workout_id_to_user():
    collection_mock = MagicMock()
    collection_mock.find_one_and_update.return_value = {
        "_id": ObjectId("60f992a7a717e93c95eab4de"),
        "workouts": [],
    }

    WorkoutService.apply_workout_id_to_user(
        collection_mock, "60f992a7a717e93c95eab4de", "75fedb7a8433a888c1aca57d"
    )

    collection_mock.find_one_and_update.assert_called_once_with(
        {"_id": ObjectId("75fedb7a8433a888c1aca57d")},
        {"$push": {"workouts": "60f992a7a717e93c95eab4de"}},
        return_document=True,
    )


def test_apply_workout_id_to_user_user_not_found():
    collection_mock = MagicMock()
    collection_mock.find_one_and_update.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        WorkoutService.apply_workout_id_to_user(
            collection_mock, "60f992a7a717e93c95eab4de", "75fedb7a8433a888c1aca57d"
        )

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "404: User not found"


def test_remove_workout_id_from_user():
    collection_mock = MagicMock()
    collection_mock.find_one_and_update.return_value = {
        "_id": ObjectId("60f992a7a717e93c95eab4de"),
        "workouts": ["60f992a7a717e93c95eab4de"],
    }

    WorkoutService.remove_workout_id_from_user(
        collection_mock, "60f992a7a717e93c95eab4de", "75fedb7a8433a888c1aca57d"
    )

    collection_mock.find_one_and_update.assert_called_once_with(
        {"_id": ObjectId("75fedb7a8433a888c1aca57d")},
        {"$pull": {"workouts": "60f992a7a717e93c95eab4de"}},
        return_document=True,
    )


def test_remove_workout_id_from_user_user_not_found():
    collection_mock = MagicMock()
    collection_mock.find_one_and_update.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        WorkoutService.remove_workout_id_from_user(
            collection_mock, "60f992a7a717e93c95eab4de", "75fedb7a8433a888c1aca57d"
        )

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "404: User not found"
