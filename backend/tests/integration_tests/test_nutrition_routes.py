from backend.main import app
from fastapi.testclient import TestClient
from bson import ObjectId


client = TestClient(app)


def test_get_all_nutrition_200(clean_db):
    response = client.get("/api/nutrition")
    response_data = response.json()

    assert response.status_code == 200
    for response in response_data:
        assert "id" in response
        assert isinstance(response["id"], str)
        assert ObjectId.is_valid(response["id"])
        assert "date_created" in response
        assert isinstance(response["date_created"], str)
        assert "fat" in response
        assert isinstance(response["fat"], int)
        assert "carbs" in response
        assert isinstance(response["date_created"], int)
        assert "protein" in response
        assert isinstance(response["protein"], int)
        assert "total" in response
        assert isinstance(response["total"], int)
        assert "body" in response
        assert isinstance(response["body"], dict)
