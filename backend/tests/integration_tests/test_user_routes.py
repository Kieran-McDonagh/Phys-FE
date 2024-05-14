from bson import ObjectId

# # CREATE


def test_post_user_200(clean_db, test_client):
    user_to_post = {
        "username": "foo",
        "email": "bar@email.com",
        "password": "foobar",
        "full_name": "foo bar",
    }

    response = test_client.post("/api/users", json=user_to_post)
    response_data = response.json()

    assert response.status_code == 201
    assert response_data == {"message": "User registered successfully"}


def test_post_user_422_missing_property(clean_db, test_client):
    user_to_post = {
        "email": "bar@email.com",
        "password": "foobar",
        "full_name": "foo bar",
    }

    response = test_client.post("/api/users", json=user_to_post)
    response_data = response.json()

    assert response.status_code == 422
    assert response_data["detail"][0]["type"] == "missing"
    assert response_data["detail"][0]["loc"] == ["body", "username"]
    assert response_data["detail"][0]["msg"] == "Field required"


def test_post_user_422_invalid_property(clean_db, test_client):
    user_to_post = {
        "username": "foo",
        "email": "bar.com",
        "password": "foobar",
        "full_name": "foo bar",
    }

    response = test_client.post("/api/users", json=user_to_post)
    response_data = response.json()

    assert response.status_code == 422
    assert response_data["detail"][0]["type"] == "value_error"
    assert response_data["detail"][0]["loc"] == ["body", "email"]
    assert (
        response_data["detail"][0]["msg"]
        == "value is not a valid email address: The email address is not valid. It must have exactly one @-sign."
    )


def test_post_user_201_with_extra_values(clean_db, test_client):
    user_to_post = {
        "username": "foo",
        "email": "bar@email.com",
        "password": "foobar",
        "full_name": "foo bar",
        "extra_info": "banana",
    }

    response = test_client.post("/api/users", json=user_to_post)
    response_data = response.json()

    assert response.status_code == 201
    assert response_data == {"message": "User registered successfully"}


# # READ


def test_get_all_users_200(clean_db, authorised_test_client):
    response = authorised_test_client.get("/api/users")
    response_data = response.json()
    assert response.status_code == 200
    for user in response_data:
        assert len(user) == 9
        assert "id" in user
        assert isinstance(user["id"], str)
        assert ObjectId.is_valid(user["id"])
        assert "username" in user
        assert isinstance(user["username"], str)
        assert "full_name" in user
        assert isinstance(user["full_name"], str)
        assert "email" in user
        assert isinstance(user["email"], str)
        assert "workouts" in user
        assert isinstance(user["workouts"], list)
        assert "nutrition" in user
        assert isinstance(user["nutrition"], list)
        assert "friends" in user
        assert isinstance(user["friends"], list)
        assert "hashed_password" in user
        assert isinstance(user["hashed_password"], str)
        assert "disabled" in user
        assert isinstance(user["disabled"], bool)


def test_get_all_users_401(clean_db, test_client):
    response = test_client.get("/api/users")
    response_data = response.json()
    assert response.status_code == 401
    assert response_data == {"detail": "Not authenticated"}


# def test_get_all_users_404(empty_db, authorised_test_client):
#     response = authorised_test_client.get("/api/users")
#     response_data = response.json()
#     print(response_data)

#     assert response.status_code == 404
#     assert response_data == {"detail": "Users not found"}


def test_get_all_users_with_name_query_200(clean_db, authorised_test_client):
    response = authorised_test_client.get("/api/users?username=user1")
    response_data = response.json()

    assert response.status_code == 200
    assert len(response_data) == 1

    user = response_data[0]

    assert user == {
        "id": "65fedb7a8433a888c1aca57c",
        "email": "user1@email.com",
        "workouts": [],
        "nutrition": [],
        "friends": ["75fedb7a8433a888c1aca57d", "95fedb7a8433a888c1aca57f"],
        "username": "user1",
        "full_name": "test name 1",
        "disabled": False,
        "hashed_password": "$2b$12$u7qTSdNfDzvFtAscVCmXH.cji.RiPbU5CVxJl1Eb.zzUAGG5USegW",
    }


# def test_get_all_users_with_name_query_404(clean_db):
#     response = client.get("/api/users?name=doesnt_exist")
#     response_data = response.json()

#     assert response.status_code == 404
#     assert response_data == {"detail": "Users not found"}


# def test_get_user_by_id_200(clean_db):
#     response = client.get("/api/users/65fedb7a8433a888c1aca57c")
#     response_data = response.json()

#     assert response.status_code == 200
#     assert response_data == {
#         "id": "65fedb7a8433a888c1aca57c",
#         "name": "user1",
#         "email": "user1@email.com",
#         "workouts": [],
#         "friends": ["75fedb7a8433a888c1aca57d", "95fedb7a8433a888c1aca57f"],
#     }


# def test_get_user_by_id_404(clean_db):
#     response = client.get("/api/users/15fedb7a8433a888c1aca57c")
#     response_data = response.json()

#     assert response.status_code == 404
#     assert response_data == {"detail": "User not found"}


# def test_get_user_by_id_400(clean_db):
#     response = client.get("/api/users/invalidid")
#     response_data = response.json()

#     assert response.status_code == 400
#     assert response_data == {"detail": "Invalid id"}


# # UPDATE


# def test_update_user_201(clean_db):
#     updated_user = {
#         "name": "foo",
#         "email": "fighter@email.com",
#         "workouts": ["65fedb7a8433a888c1aca57c"],
#         "friends": ["75fedb7a8433a888c1aca57d", "95fedb7a8433a888c1aca57f"],
#     }

#     response = client.put("/api/users/85fedb7a8433a888c1aca57e", json=updated_user)
#     response_data = response.json()

#     assert response.status_code == 201
#     assert response_data == {
#         "id": "85fedb7a8433a888c1aca57e",
#         "name": "foo",
#         "email": "fighter@email.com",
#         "workouts": ["65fedb7a8433a888c1aca57c"],
#         "friends": ["75fedb7a8433a888c1aca57d", "95fedb7a8433a888c1aca57f"],
#     }


# def test_update_user_404(clean_db):
#     updated_user = {
#         "name": "foo",
#         "email": "fighter@email.com",
#         "workouts": [],
#         "friends": [],
#     }

#     response = client.put("/api/users/85fedb7a8433a888c1aca57f", json=updated_user)
#     response_data = response.json()

#     assert response.status_code == 404
#     assert response_data == {"detail": "User not found"}


# def test_update_user_400(clean_db):
#     updated_user = {"name": "foo", "email": "fighter@email.com", "workouts": []}

#     response = client.put("/api/users/invalidid", json=updated_user)
#     response_data = response.json()

#     assert response.status_code == 400
#     assert response_data == {"detail": "Invalid id"}


# def test_update_user_422_invalid_property(clean_db):
#     updated_user = {
#         "not_a_name": "foo",
#         "email": "fighter@email.com",
#         "workouts": [],
#         "friends": [],
#     }

#     response = client.put("/api/users/85fedb7a8433a888c1aca57e", json=updated_user)
#     response_data = response.json()

#     assert response.status_code == 422
#     assert response_data["detail"][0]["type"] == "missing"
#     assert response_data["detail"][0]["loc"] == ["body", "name"]
#     assert response_data["detail"][0]["msg"] == "Field required"


# def test_update_user_422_invalid_property_value(clean_db):
#     updated_user = {
#         "name": "foo",
#         "email": "email.com",
#     }

#     response = client.put("/api/users/85fedb7a8433a888c1aca57e", json=updated_user)
#     response_data = response.json()

#     assert response.status_code == 422
#     assert response_data["detail"][0]["type"] == "value_error"
#     assert response_data["detail"][0]["loc"] == ["body", "email"]
#     assert (
#         response_data["detail"][0]["msg"]
#         == "value is not a valid email address: The email address is not valid. It must have exactly one @-sign."
#     )


# def test_update_user_422_missing_property(clean_db):
#     updated_user = {
#         "email": "fighter@email.com",
#     }

#     response = client.put("/api/users/85fedb7a8433a888c1aca57e", json=updated_user)
#     response_data = response.json()

#     assert response.status_code == 422
#     assert response_data["detail"][0]["type"] == "missing"
#     assert response_data["detail"][0]["loc"] == ["body", "name"]
#     assert response_data["detail"][0]["msg"] == "Field required"


# def test_update_user_201_with_ignored_value(clean_db):
#     updated_user = {
#         "name": "foo",
#         "email": "fighter@email.com",
#         "extra_value": "doesnt matter",
#         "workouts": ["65fedb7a8433a888c1aca57c"],
#         "friends": [],
#     }

#     response = client.put("/api/users/85fedb7a8433a888c1aca57e", json=updated_user)
#     response_data = response.json()

#     assert response.status_code == 201
#     assert response_data == {
#         "id": "85fedb7a8433a888c1aca57e",
#         "name": "foo",
#         "email": "fighter@email.com",
#         "workouts": ["65fedb7a8433a888c1aca57c"],
#         "friends": [],
#     }


# # DELETE


# def test_delete_user_200(clean_db):
#     response = client.delete("/api/users/75fedb7a8433a888c1aca57d")
#     response_data = response.json()

#     assert response.status_code == 200
#     assert response_data == {
#         "id": "75fedb7a8433a888c1aca57d",
#         "name": "user2",
#         "email": "user2@email.com",
#         "workouts": ["65fedb7a8433a888c1aca57a", "65fedb7a8433a888c1aca57b"],
#         "friends": ["65fedb7a8433a888c1aca57c", "95fedb7a8433a888c1aca57f"],
#     }


# def test_deleted_user_not_in_friends_list(clean_db):
#     client.delete("/api/users/75fedb7a8433a888c1aca57d")
#     all_users = client.get("/api/users")
#     response_data = all_users.json()

#     for user in response_data:
#         assert "75fedb7a8433a888c1aca57d" not in user["friends"]


# def test_delete_user_with_no_friends(clean_db):
#     response = client.delete("/api/users/85fedb7a8433a888c1aca57e")
#     response_data = response.json()

#     assert response.status_code == 200
#     assert response_data == {
#         "id": "85fedb7a8433a888c1aca57e",
#         "name": "user3",
#         "email": "user3@email.com",
#         "workouts": ["65fedb7a8433a888c1aca57c"],
#         "friends": [],
#     }


# def test_delete_user_404(clean_db):
#     response = client.delete("/api/users/65fedb7a8433a888c1aca57a")
#     response_data = response.json()

#     assert response.status_code == 404
#     assert response_data == {"detail": "User not found"}


# def test_delete_user_400(clean_db):
#     response = client.delete("/api/users/invalidid")
#     response_data = response.json()

#     assert response.status_code == 400
#     assert response_data == {"detail": "Invalid id"}
