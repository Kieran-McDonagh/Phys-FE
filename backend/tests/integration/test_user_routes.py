import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.tests.utils.clean_collection import CleanDatabase

client = TestClient(app)
cleaner = CleanDatabase()


@pytest.mark.asyncio
async def test_get_all_users():
    await cleaner.clean_user_collection()
    response = client.get("/api/user")
    response_data = response.json()
    assert response.status_code == 200

    users = response_data[1]["data"]["all_users"]
    for user in users:
        assert "_id" in user
        assert isinstance(user["_id"], str)

        assert "name" in user
        assert isinstance(user["name"], str)

        assert "email" in user
        assert isinstance(user["email"], str)
