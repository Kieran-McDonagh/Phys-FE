from backend.main import app
from fastapi.testclient import TestClient
from bson import ObjectId


client = TestClient(app)


def test_get_all_workouts_200(clean_db):
    response = client.get("/api/workouts")
    response_data = response.json()

    assert response.status_code == 200
    for workout in response_data:
        assert "id" in workout
        assert isinstance(workout["id"], str)
        assert ObjectId.is_valid(workout["id"])
        assert "type" in workout
        assert isinstance(workout["type"], str)
        assert "title" in workout
        assert isinstance(workout["title"], str)
        assert "body" in workout
        assert isinstance(workout["body"], dict)
        assert "author_id" in workout
        assert isinstance(workout["author_id"], str)
        assert ObjectId.is_valid(workout["author_id"])
        assert "date_created" in workout
        assert isinstance(workout["date_created"], str)
        
