import pytest
from unittest.mock import MagicMock
from backend.services.user_service import UserService


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
