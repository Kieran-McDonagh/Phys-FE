import pytest
from backend.database.connection import MongoConnection
from backend.database.seeding.seed_user_data import user_data
from backend.database.seeding.seed_workouts_data import workouts_data


@pytest.fixture(scope="function")
def clean_db():
    test_db = MongoConnection()
    test_db.drop_collection("users")
    test_db.drop_collection("workouts")
    test_db.seed_collection("users", user_data)
    test_db.seed_collection("workouts", workouts_data)

    yield test_db


@pytest.fixture(scope="function")
def empty_db():
    test_db = MongoConnection()
    test_db.drop_collection("users")
    test_db.drop_collection("workouts")

    yield test_db
