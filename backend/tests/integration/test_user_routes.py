from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_all_users():
    response = client.get("/api/user/")
    print(response.json())
    