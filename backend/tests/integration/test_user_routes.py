import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.tests.utils.clean_collection import CleanTestDatabase

client = TestClient(app)
clean_test_database = CleanTestDatabase()

@pytest.fixture
def clean_db():
    clean_test_database.clean_user_collection()

def test_get_all_users(clean_db):
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
        

def test_get_user_by_id(clean_db):
    # build a user with the user builder
    response = client.get(f"/api/user/{id}")
    response_data = response.json()
    
    print(response_data)
