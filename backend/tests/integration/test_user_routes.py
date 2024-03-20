import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.connection import MongoConnection
from backend.tests.test_data.users import users

client = TestClient(app)

async def clean_collection():
    connection = MongoConnection()
    await connection.drop_collection("users")
    await connection.seed_users(users)

@pytest.mark.asyncio
async def test_example():
    await clean_collection()
    response = client.get("/api/user")
    print(response.json())
    assert True
    




