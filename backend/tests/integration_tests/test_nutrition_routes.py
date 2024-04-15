from backend.main import app
from fastapi.testclient import TestClient
from bson import ObjectId


client = TestClient(app)


def test_get_all_nutrition_200(clean_db):
    response = client.get("/api/nutrition")
    response_data = response.json()

    assert response.status_code == 200
    for response in response_data:
        assert len(response) == 8
        assert "id" in response
        assert isinstance(response["id"], str)
        assert ObjectId.is_valid(response["id"])
        assert "date" in response
        assert isinstance(response["date"], str)
        assert "fat" in response
        assert isinstance(response["fat"], int)
        assert "carbs" in response
        assert isinstance(response["carbs"], int)
        assert "protein" in response
        assert isinstance(response["protein"], int)
        assert "total_calories" in response
        assert isinstance(response["total_calories"], int)
        assert "body" in response
        assert isinstance(response["body"], dict)
        assert "user_id" in response
        assert isinstance(response["user_id"], str)
        assert ObjectId.is_valid(response["user_id"])


def test_get_all_nutrition_by_user_id_200(clean_db):
    response = client.get("/api/nutrition?user_id=75fedb7a8433a888c1aca57d")
    response_data = response.json()

    assert response.status_code == 200
    assert len(response_data) == 3
    for response in response_data:
        assert len(response) == 8
        assert "id" in response
        assert isinstance(response["id"], str)
        assert ObjectId.is_valid(response["id"])
        assert "date" in response
        assert isinstance(response["date"], str)
        assert "fat" in response
        assert isinstance(response["fat"], int)
        assert "carbs" in response
        assert isinstance(response["carbs"], int)
        assert "protein" in response
        assert isinstance(response["protein"], int)
        assert "total_calories" in response
        assert isinstance(response["total_calories"], int)
        assert "body" in response
        assert isinstance(response["body"], dict)
        assert "user_id" in response
        assert isinstance(response["user_id"], str)
        assert ObjectId.is_valid(response["user_id"])


def test_get_all_nutrition_404(empty_db):
    response = client.get("/api/nutrition")
    response_data = response.json()

    assert response.status_code == 404
    assert response_data == {"detail": "Nutrition data not found"}
