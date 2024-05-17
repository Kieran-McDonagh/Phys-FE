import pytest
from backend.database.connection import MongoConnection
from backend.database.seeding.seed_user_data import user_data
from backend.database.seeding.seed_workouts_data import workouts_data
from backend.database.seeding.seed_nutrition_data import nutrition_data
from backend.database.seeding.authorised_user_data.seed_authorised_user_workouts import (
    authorised_user_workouts,
)
from backend.main import app
from fastapi.testclient import TestClient
from bson import ObjectId

test_db = MongoConnection()


@pytest.fixture(scope="function")
def clean_db():
    test_db.drop_collection("users")
    test_db.drop_collection("workouts")
    test_db.drop_collection("nutrition")

    test_db.seed_collection("users", user_data)
    test_db.seed_collection("workouts", workouts_data)
    test_db.seed_collection("nutrition", nutrition_data)

    yield test_db


@pytest.fixture(scope="function")
def empty_db():
    test_db.drop_collection("users")
    test_db.drop_collection("workouts")
    test_db.drop_collection("nutrition")

    yield test_db


@pytest.fixture(scope="function")
def client():
    test_client = TestClient(app)
    return test_client


@pytest.fixture(scope="function")
def authorised_test_client(client):
    user_to_post = {
        "username": "test user",
        "email": "test_user@email.com",
        "password": "test password",
        "full_name": "test user",
    }

    response = client.post("/api/users", json=user_to_post)
    authorised_user = response.json()

    login_data = {"username": "test user", "password": "test password"}
    login_response = client.post("/token", data=login_data)
    assert login_response.status_code == 200
    access_token = login_response.json()["access_token"]

    client.headers.update({"Authorization": f"Bearer {access_token}"})

    workout_data = authorised_user_workouts(authorised_user["id"])

    test_db.seed_collection("workouts", workout_data)

    return client, authorised_user


@pytest.fixture(scope="function")
def authorised_workouts(authorised_test_client):
    test_db = MongoConnection()
    user_collection = test_db.get_collection("users")
    _, user = authorised_test_client
    user["workouts"].append("83fedb6a8433a888c1aca37d")

    user_collection.find_one_and_update(
        {"_id": ObjectId(user["id"])}, {"$set": user}, return_document=True
    )
