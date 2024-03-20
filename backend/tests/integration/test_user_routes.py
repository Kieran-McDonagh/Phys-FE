import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.connection import user_collection

client = TestClient(app)

@pytest.mark.asyncio
async def seed_db():
    await user_collection.drop()
    await user_collection.insert_one({"name": "foo", "email": "bar@email.com"})

@pytest.mark.asyncio
async def test_read_item():
    response = client.get("/api/user/")
    print(response.json())









