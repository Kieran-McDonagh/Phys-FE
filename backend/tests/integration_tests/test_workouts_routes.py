from backend.main import app
from fastapi.testclient import TestClient
from bson import ObjectId


client = TestClient(app)

# CREATE


def test_post_workout_201(clean_db):
    workout_to_post = {
        "type": "individual",
        "title": "test post workout",
        "body": {"exercise 1": "10", "exercise 2": "20", "exercise 3": "30"},
        "user_id": "75fedb7a8433a888c1aca57d",
    }
    response = client.post("/api/workouts", json=workout_to_post)
    response_data = response.json()

    assert response.status_code == 201
    assert len(response_data) == 6
    assert "id" in response_data
    assert isinstance(response_data["id"], str)
    assert ObjectId.is_valid(response_data["id"])
    assert "date_created" in response_data
    assert isinstance(response_data["date_created"], str)
    assert response_data["type"] == "individual"
    assert response_data["title"] == "test post workout"
    assert response_data["body"] == {
        "exercise 1": "10",
        "exercise 2": "20",
        "exercise 3": "30",
    }
    assert response_data["user_id"] == "75fedb7a8433a888c1aca57d"

    user_to_check = client.get("/api/users/75fedb7a8433a888c1aca57d")
    user_data = user_to_check.json()

    assert response_data["id"] in user_data["workouts"]


def test_post_workout_404(clean_db):
    workout_to_post = {
        "type": "individual",
        "title": "test post workout",
        "body": {"exercise 1": "10", "exercise 2": "20", "exercise 3": "30"},
        "user_id": "38bedb7a8433a888c1aca57e",
    }
    response = client.post("/api/workouts", json=workout_to_post)
    response_data = response.json()

    assert response.status_code == 500
    assert response_data == {
        "detail": "Failed to add workout to user, 500: Failed to apply workout ID to user: 404: User not found"
    }


def test_post_workout_422_missing_property(clean_db):
    workout_to_post = {
        "type": "individual",
        "body": {"exercise 1": "10", "exercise 2": "20", "exercise 3": "30"},
        "user_id": "75fedb7a8433a888c1aca57d",
    }
    response = client.post("/api/workouts", json=workout_to_post)
    response_data = response.json()

    assert response.status_code == 422
    assert response_data["detail"][0]["type"] == "missing"
    assert response_data["detail"][0]["loc"] == ["body", "title"]
    assert response_data["detail"][0]["msg"] == "Field required"


def test_post_workout_422_invalid_property(clean_db):
    workout_to_post = {
        "type": "banana",
        "title": "test incorrect type",
        "body": {"exercise 1": "10", "exercise 2": "20", "exercise 3": "30"},
        "user_id": "75fedb7a8433a888c1aca57d",
    }
    response = client.post("/api/workouts", json=workout_to_post)
    response_data = response.json()

    assert response.status_code == 422
    assert response_data["detail"][0]["type"] == "value_error"
    assert response_data["detail"][0]["loc"] == ["body", "type"]
    assert (
        response_data["detail"][0]["msg"]
        == "Value error, type must be one of ('individual', 'battlephys')"
    )


def test_post_workout_422_invalid_user_id(clean_db):
    workout_to_post = {
        "type": "battlephys",
        "title": "test incorrect type",
        "body": {"exercise 1": "10", "exercise 2": "20", "exercise 3": "30"},
        "user_id": "banana",
    }
    response = client.post("/api/workouts", json=workout_to_post)
    response_data = response.json()

    assert response.status_code == 422
    assert response_data["detail"][0]["type"] == "value_error"
    assert response_data["detail"][0]["loc"] == ["body", "user_id"]
    assert (
        response_data["detail"][0]["msg"]
        == "Value error, user_id must be a valid MongoDB ObjectId"
    )


def test_post_workout_422_invalid_data_type(clean_db):
    workout_to_post = {
        "type": "battlephys",
        "title": 12345,
        "body": {"exercise 1": "10", "exercise 2": "20", "exercise 3": "30"},
        "user_id": "75fedb7a8433a888c1aca57d",
    }
    response = client.post("/api/workouts", json=workout_to_post)
    response_data = response.json()

    assert response.status_code == 422
    assert response_data["detail"][0]["type"] == "string_type"
    assert response_data["detail"][0]["loc"] == ["body", "title"]
    assert response_data["detail"][0]["msg"] == "Input should be a valid string"


# READ


def test_get_all_workouts_200(clean_db):
    response = client.get("/api/workouts")
    response_data = response.json()

    assert response.status_code == 200

    assert response_data[0]["date_created"] == "2024-04-05T20:00:00"
    assert response_data[1]["date_created"] == "2024-04-05T19:00:00"
    assert response_data[2]["date_created"] == "2024-04-05T18:00:00"

    for workout in response_data:
        assert len(workout) == 6
        assert "id" in workout
        assert isinstance(workout["id"], str)
        assert ObjectId.is_valid(workout["id"])
        assert "type" in workout
        assert isinstance(workout["type"], str)
        assert "title" in workout
        assert isinstance(workout["title"], str)
        assert "body" in workout
        assert isinstance(workout["body"], dict)
        assert "user_id" in workout
        assert isinstance(workout["user_id"], str)
        assert ObjectId.is_valid(workout["user_id"])
        assert "date_created" in workout
        assert isinstance(workout["date_created"], str)


def test_get_all_workouts_404(empty_db):
    response = client.get("/api/workouts")
    response_data = response.json()

    assert response.status_code == 404
    assert response_data == {"detail": "Workouts not found"}


def test_get_all_workouts_with_user_id_query_200(clean_db):
    response = client.get("/api/workouts?user_id=75fedb7a8433a888c1aca57d")
    response_data = response.json()

    assert response.status_code == 200
    for workout in response_data:
        assert len(workout) == 6
        assert "id" in workout
        assert isinstance(workout["id"], str)
        assert ObjectId.is_valid(workout["id"])
        assert "type" in workout
        assert isinstance(workout["type"], str)
        assert "title" in workout
        assert isinstance(workout["title"], str)
        assert "body" in workout
        assert isinstance(workout["body"], dict)
        assert "user_id" in workout
        assert isinstance(workout["user_id"], str)
        assert ObjectId.is_valid(workout["user_id"])
        assert "date_created" in workout
        assert isinstance(workout["date_created"], str)


def test_get_all_workouts_with_user_id_query_404(clean_db):
    response = client.get("/api/workouts?user_id=65fedb7a8433a888c1aca57c")
    response_data = response.json()

    assert response.status_code == 404
    assert response_data == {"detail": "Workouts not found"}


def test_get_all_workouts_with_user_id_query_400(clean_db):
    response = client.get("/api/workouts?user_id=banana")
    response_data = response.json()

    assert response.status_code == 400
    assert response_data == {"detail": "Invalid id"}


def test_get_workouts_sort_by_ascending_200(clean_db):
    response = client.get("/api/workouts?sort_by_date=False")
    response_data = response.json()

    assert response.status_code == 200
    assert response_data[0]["date_created"] == "2024-04-05T18:00:00"
    assert response_data[1]["date_created"] == "2024-04-05T19:00:00"
    assert response_data[2]["date_created"] == "2024-04-05T20:00:00"


def test_get_workout_by_id_200(clean_db):
    response = client.get("/api/workouts/65fedb7a8433a888c1aca57a")
    response_data = response.json()

    assert response.status_code == 200
    assert response_data == {
        "id": "65fedb7a8433a888c1aca57a",
        "type": "individual",
        "title": "title 1",
        "body": {"exercise 1": "10", "exercise 2": "10", "exercise 3": "10"},
        "user_id": "75fedb7a8433a888c1aca57d",
        "date_created": "2024-04-05T18:00:00",
    }


def test_get_workout_by_id_404(empty_db):
    response = client.get("/api/workouts/65fedb7a8433a888c1aca57a")
    response_data = response.json()

    assert response.status_code == 404
    assert response_data == {"detail": "workout not found"}


def test_get_workout_by_id_400(clean_db):
    response = client.get("/api/workouts/banana")
    response_data = response.json()

    assert response.status_code == 400
    assert response_data == {"detail": "Invalid id"}


# UPDATE


def test_update_workout_201(clean_db):
    updated_workout = {
        "type": "battlephys",
        "title": "title 4",
        "body": {"exercise 1": "10", "exercise 2": "10", "new exercise": "10"},
        "user_id": "85fedb7a8433a888c1aca57e",
    }
    response = client.put("api/workouts/65fedb7a8433a888c1aca57c", json=updated_workout)
    response_data = response.json()

    assert response.status_code == 201
    assert response_data == {
        "id": "65fedb7a8433a888c1aca57c",
        "type": "battlephys",
        "title": "title 4",
        "body": {"exercise 1": "10", "exercise 2": "10", "new exercise": "10"},
        "user_id": "85fedb7a8433a888c1aca57e",
        "date_created": "2024-04-05T20:00:00",
    }


def test_update_workout_additional_properties_201(clean_db):
    updated_workout = {
        "type": "individual",
        "title": "title 4",
        "body": {"exercise 1": "10", "exercise 2": "10", "exercise 3": "10"},
        "user_id": "85fedb7a8433a888c1aca57e",
        "foo": "bar",
    }
    response = client.put("api/workouts/65fedb7a8433a888c1aca57c", json=updated_workout)
    response_data = response.json()

    assert response.status_code == 201
    assert response_data == {
        "id": "65fedb7a8433a888c1aca57c",
        "type": "individual",
        "title": "title 4",
        "body": {"exercise 1": "10", "exercise 2": "10", "exercise 3": "10"},
        "user_id": "85fedb7a8433a888c1aca57e",
        "date_created": "2024-04-05T20:00:00",
    }


def test_update_workout_404(clean_db):
    updated_workout = {
        "type": "individual",
        "title": "title 4",
        "body": {"exercise 1": "10", "exercise 2": "10", "exercise 3": "10"},
        "user_id": "85fedb7a8433a888c1aca57e",
    }
    response = client.put("api/workouts/47fedb7a8433a888c1aca57c", json=updated_workout)
    response_data = response.json()

    assert response.status_code == 404
    assert response_data == {"detail": "Workout not found"}


def test_update_workout_400(clean_db):
    updated_workout = {
        "type": "individual",
        "title": "title 4",
        "body": {"exercise 1": "10", "exercise 2": "10", "exercise 3": "10"},
        "user_id": "85fedb7a8433a888c1aca57e",
    }
    response = client.put("api/workouts/banana", json=updated_workout)
    response_data = response.json()

    assert response.status_code == 400
    assert response_data == {"detail": "Invalid id"}


def test_update_workout_422_missing_property(clean_db):
    updated_workout = {
        "type": "individual",
        "title": "title 4",
        "user_id": "85fedb7a8433a888c1aca57e",
    }
    response = client.put("api/workouts/65fedb7a8433a888c1aca57c", json=updated_workout)
    response_data = response.json()

    assert response.status_code == 422
    assert response_data["detail"][0]["type"] == "missing"
    assert response_data["detail"][0]["loc"] == ["body", "body"]
    assert response_data["detail"][0]["msg"] == "Field required"


def test_update_workout_422_invalid_property(clean_db):
    updated_workout = {
        "type": "individual",
        "title": "title 4",
        "body": "foo",
        "user_id": "85fedb7a8433a888c1aca57e",
    }
    response = client.put("api/workouts/65fedb7a8433a888c1aca57c", json=updated_workout)
    response_data = response.json()

    assert response.status_code == 422
    assert response_data["detail"][0]["type"] == "dict_type"
    assert response_data["detail"][0]["loc"] == ["body", "body"]
    assert response_data["detail"][0]["msg"] == "Input should be a valid dictionary"


# DELETE


def test_delete_workout_200(clean_db):
    response = client.delete("api/workouts/65fedb7a8433a888c1aca57c")
    response_data = response.json()

    assert response.status_code == 200
    assert response_data == {
        "id": "65fedb7a8433a888c1aca57c",
        "type": "battlephys",
        "title": "title 3",
        "body": {"exercise 1": "10", "exercise 2": "10", "exercise 3": "10"},
        "user_id": "85fedb7a8433a888c1aca57e",
        "date_created": "2024-04-05T20:00:00",
    }


def test_delete_workout_404(clean_db):
    response = client.delete("api/workouts/13fedb7a8433a888c1aca57c")
    response_data = response.json()

    assert response.status_code == 404
    assert response_data == {"detail": "Workout not found"}


def test_delete_workout_400(clean_db):
    response = client.delete("api/workouts/banana")
    response_data = response.json()

    assert response.status_code == 400
    assert response_data == {"detail": "Invalid id"}
