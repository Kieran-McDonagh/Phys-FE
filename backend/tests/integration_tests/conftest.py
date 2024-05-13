import pytest
from backend.database.connection import MongoConnection
from backend.database.seeding.seed_user_data import user_data
from backend.database.seeding.seed_workouts_data import workouts_data
from backend.database.seeding.seed_nutrition_data import nutrition_data
from backend.main import app
from fastapi.testclient import TestClient


@pytest.fixture(scope="function")
def clean_db():
    test_db = MongoConnection()
    test_db.drop_collection("users")
    test_db.drop_collection("workouts")
    test_db.drop_collection("nutrition")

    test_db.seed_collection("users", user_data)
    test_db.seed_collection("workouts", workouts_data)
    test_db.seed_collection("nutrition", nutrition_data)

    yield test_db


@pytest.fixture(scope="function")
def empty_db():
    test_db = MongoConnection()
    test_db.drop_collection("users")
    test_db.drop_collection("workouts")
    test_db.drop_collection("nutrition")

    yield test_db


@pytest.fixture(scope="function")
def test_client():
    test_client = TestClient(app)
    return test_client


@pytest.fixture(scope="function")
def authorised_test_client(test_client):
    user_to_post = {
        "username": "test user",
        "email": "test_user@email.com",
        "password": "test password",
        "full_name": "test user",
    }

    test_client.post("/api/users", json=user_to_post)

    login_data = {"username": "test user", "password": "test password"}
    login_response = test_client.post("/token", data=login_data)
    assert login_response.status_code == 200
    access_token = login_response.json()["access_token"]

    test_client.headers.update({"Authorization": f"Bearer {access_token}"})

    return test_client
