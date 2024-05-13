import pytest
from unittest.mock import MagicMock
from backend.services.user_service import UserService
from unittest.mock import patch
from bson import ObjectId
from fastapi import HTTPException


@pytest.mark.asyncio
async def test_remove_user_from_all_friends_lists():
    collection_mock = MagicMock()
    user_id = "user123"

    await UserService.remove_user_from_all_friends_lists(collection_mock, user_id)

    collection_mock.update_many.assert_called_once_with(
        {"friends": user_id}, {"$pull": {"friends": user_id}}
    )


@pytest.mark.asyncio
async def test_remove_user_from_all_friends_lists_exception(capsys):
    collection_mock = MagicMock()
    collection_mock.update_many.side_effect = Exception("Some error")
    user_id = "user123"

    await UserService.remove_user_from_all_friends_lists(collection_mock, user_id)

    collection_mock.update_many.assert_called_once()
    assert (
        "An error occurred while removing user from friends lists"
        in capsys.readouterr().out
    )


def test_apply_document_id_to_user():
    collection_mock = MagicMock()
    collection_mock.find_one_and_update.return_value = {
        "_id": ObjectId("60f992a7a717e93c95eab4de"),
        "workouts": [],
    }

    UserService.apply_document_id_to_user(
        collection_mock, "60f992a7a717e93c95eab4de", "75fedb7a8433a888c1aca57d", 'workouts'
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
        UserService.apply_document_id_to_user(
            collection_mock, "60f992a7a717e93c95eab4de", "75fedb7a8433a888c1aca57d", 'workouts'
        )

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "404: User not found"


def test_remove_document_id_from_user():
    collection_mock = MagicMock()
    collection_mock.find_one_and_update.return_value = {
        "_id": ObjectId("60f992a7a717e93c95eab4de"),
        "workouts": ["60f992a7a717e93c95eab4de"],
    }

    UserService.remove_document_id_from_user(
        collection_mock, "60f992a7a717e93c95eab4de", "75fedb7a8433a888c1aca57d", 'workouts'
    )

    collection_mock.find_one_and_update.assert_called_once_with(
        {"_id": ObjectId("75fedb7a8433a888c1aca57d")},
        {"$pull": {"workouts": "60f992a7a717e93c95eab4de"}},
        return_document=True,
    )


def test_remove_document_id_from_user_user_not_found():
    collection_mock = MagicMock()
    collection_mock.find_one_and_update.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        UserService.remove_document_id_from_user(
            collection_mock, "60f992a7a717e93c95eab4de", "75fedb7a8433a888c1aca57d", 'workouts'
        )

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "404: User not found"

