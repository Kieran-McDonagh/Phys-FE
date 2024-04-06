from backend.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_all_users_200(clean_db):
    response = client.get("/api/users")
    response_data = response.json()

    assert response.status_code == 200
    for user in response_data:
        assert "_id" in user
        assert isinstance(user["_id"], str)
        assert "name" in user
        assert isinstance(user["name"], str)
        assert "email" in user
        assert isinstance(user["email"], str)
        assert "workouts" in user
        assert isinstance(user["workouts"], list)


def test_get_all_users_404(empty_db):
    response = client.get("/api/users")
    response_data = response.json()

    assert response.status_code == 404
    assert response_data == {"detail": "Users not found"}


def test_get_user_by_id_200(clean_db):
    response = client.get("/api/users/65fedb7a8433a888c1aca57c")
    response_data = response.json()

    assert response.status_code == 200
    assert response_data == {
        "_id": "65fedb7a8433a888c1aca57c",
        "name": "user1",
        "email": "user1@email.com",
        "workouts": [],
    }


def test_get_user_by_id_404(clean_db):
    response = client.get("/api/users/15fedb7a8433a888c1aca57c")
    response_data = response.json()

    assert response.status_code == 404
    assert response_data == {"detail": "User not found"}


def test_get_user_by_id_400(clean_db):
    response = client.get("/api/users/invalid_id")
    response_data = response.json()

    assert response.status_code == 400
    assert response_data == {"detail": "Invalid id"}


def test_post_user_200(clean_db):
    user_to_post = {"name": "foo", "email": "bar@email.com"}

    response = client.post("/api/users", json=user_to_post)
    response_data = response.json()

    assert response.status_code == 201
    assert response_data["_id"]
    assert response_data["name"] == "foo"
    assert response_data["email"] == "bar@email.com"
    assert response_data["workouts"] == []


def test_post_user_422_missing_property(clean_db):
    user_to_post = {"email": "bar@email.com"}

    response = client.post("/api/users", json=user_to_post)
    response_data = response.json()

    assert response.status_code == 422
    assert response_data["detail"][0]["type"] == "missing"
    assert response_data["detail"][0]["loc"] == ["body", "name"]
    assert response_data["detail"][0]["msg"] == "Field required"


def test_post_user_422_invalid_property(clean_db):
    user_to_post = {"name": "foo", "email": "email.com"}

    response = client.post("/api/users", json=user_to_post)
    response_data = response.json()

    assert response.status_code == 422
    assert response_data["detail"][0]["type"] == "value_error"
    assert response_data["detail"][0]["loc"] == ["body", "email"]
    assert (
        response_data["detail"][0]["msg"]
        == "value is not a valid email address: The email address is not valid. It must have exactly one @-sign."
    )


def test_post_user_201_with_extra_values(clean_db):
    user_to_post = {
        "name": "extra_info",
        "email": "bar@email.com",
        "extra_property": "doesnt matter",
    }

    response = client.post("/api/users", json=user_to_post)
    response_data = response.json()

    assert response.status_code == 201
    assert response_data["_id"]
    assert response_data["name"] == "extra_info"
    assert response_data["email"] == "bar@email.com"
    assert response_data["workouts"] == []
    assert "extra_property" not in response_data


def test_update_user_201(clean_db):
    updated_user = {
        "name": "foo",
        "email": "fighter@email.com",
        "workouts": ["65fedb7a8433a888c1aca57c"],
    }

    response = client.put("/api/users/85fedb7a8433a888c1aca57e", json=updated_user)
    response_data = response.json()

    assert response.status_code == 201
    assert response_data == {
        "_id": "85fedb7a8433a888c1aca57e",
        "name": "foo",
        "email": "fighter@email.com",
        "workouts": ["65fedb7a8433a888c1aca57c"],
    }


def test_update_user_404(clean_db):
    updated_user = {"name": "foo", "email": "fighter@email.com", "workouts": []}

    response = client.put("/api/users/85fedb7a8433a888c1aca57f", json=updated_user)
    response_data = response.json()

    assert response.status_code == 404
    assert response_data == {"detail": "User not found"}


def test_update_user_400(clean_db):
    updated_user = {"name": "foo", "email": "fighter@email.com", "workouts": []}

    response = client.put("/api/users/invalid_id", json=updated_user)
    response_data = response.json()

    assert response.status_code == 400
    assert response_data == {"detail": "Invalid id"}


def test_update_user_422_invalid_property(clean_db):
    updated_user = {"not_a_name": "foo", "email": "fighter@email.com", "workouts": []}

    response = client.put("/api/users/85fedb7a8433a888c1aca57e", json=updated_user)
    response_data = response.json()

    assert response.status_code == 422
    assert response_data["detail"][0]["type"] == "missing"
    assert response_data["detail"][0]["loc"] == ["body", "name"]
    assert response_data["detail"][0]["msg"] == "Field required"


def test_update_user_422_invalid_property_value(clean_db):
    updated_user = {
        "name": "foo",
        "email": "email.com",
    }

    response = client.put("/api/users/85fedb7a8433a888c1aca57e", json=updated_user)
    response_data = response.json()

    assert response.status_code == 422
    assert response_data["detail"][0]["type"] == "value_error"
    assert response_data["detail"][0]["loc"] == ["body", "email"]
    assert (
        response_data["detail"][0]["msg"]
        == "value is not a valid email address: The email address is not valid. It must have exactly one @-sign."
    )


def test_update_user_422_missing_property(clean_db):
    updated_user = {
        "email": "fighter@email.com",
    }

    response = client.put("/api/users/85fedb7a8433a888c1aca57e", json=updated_user)
    response_data = response.json()

    assert response.status_code == 422
    assert response_data["detail"][0]["type"] == "missing"
    assert response_data["detail"][0]["loc"] == ["body", "name"]
    assert response_data["detail"][0]["msg"] == "Field required"


def test_update_user_201_with_ignored_value(clean_db):
    updated_user = {
        "name": "foo",
        "email": "fighter@email.com",
        "extra_value": "doesnt matter",
        "workouts": ["65fedb7a8433a888c1aca57c"],
    }

    response = client.put("/api/users/85fedb7a8433a888c1aca57e", json=updated_user)
    response_data = response.json()

    assert response.status_code == 201
    assert response_data == {
        "_id": "85fedb7a8433a888c1aca57e",
        "name": "foo",
        "email": "fighter@email.com",
        "workouts": ["65fedb7a8433a888c1aca57c"],
    }


def test_delete_user_200(clean_db):
    response = client.delete("/api/users/75fedb7a8433a888c1aca57d")
    response_data = response.json()

    assert response.status_code == 200
    assert response_data == {
        "_id": "75fedb7a8433a888c1aca57d",
        "name": "user2",
        "email": "user2@email.com",
        "workouts": ["65fedb7a8433a888c1aca57a", "65fedb7a8433a888c1aca57b"],
    }


def test_delete_user_404(clean_db):
    response = client.delete("/api/users/65fedb7a8433a888c1aca57a")
    response_data = response.json()

    assert response.status_code == 404
    assert response_data == {"detail": "User not found"}


def test_delete_user_400(clean_db):
    response = client.delete("/api/users/invalid_id")
    response_data = response.json()

    assert response.status_code == 400
    assert response_data == {"detail": "Invalid id"}
