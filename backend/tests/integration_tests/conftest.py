import pytest
from backend.database.connection import MongoConnection
from backend.database.seeding.seed_user_data import user_data


@pytest.fixture(scope="function")
def clean_db():
    test_db = MongoConnection()
    test_db.drop_collection("users")
    test_db.seed_collection("users", user_data)

    yield test_db


@pytest.fixture(scope="function")
def empty_db():
    test_db = MongoConnection()
    test_db.drop_collection("users")

    yield test_db
