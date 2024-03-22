import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.tests.utils.clean_collection import CleanTestDatabase

@pytest.fixture
def clean_db():
    client = TestClient(app)
    clean_test_database = CleanTestDatabase()
    # clean_test_database.clean_user_collection()
    clean_test_database.seed_user_collection()
    yield client

def test_get_all_users(clean_db):
    response = clean_db.get("/api/user")
    assert response.status_code == 200

    response_data = response.json()
    users = response_data[1]["data"]["all_users"]
    assert len(users) == 3

    for user in users:
        assert "_id" in user
        assert isinstance(user["_id"], str)

        assert "name" in user
        assert isinstance(user["name"], str)

        assert "email" in user
        assert isinstance(user["email"], str)

    assert users[0] == {
        "_id": "65fd4a327815dc4844087c44",
        "name": "foo1",
        "email": "bar1@email.com",
    }
    assert users[1] == {
        "_id": "65fd4a327815dc4844087c45",
        "name": "foo2",
        "email": "bar2@email.com",
    }
    assert users[2] == {
        "_id": "65fd4a327815dc4844087c46",
        "name": "foo3",
        "email": "bar3@email.com",
    }