from bson import ObjectId


def authorised_user_workouts(user_id):
    return (
        {
            "_id": ObjectId("83fedb6a8433a888c1aca37d"),
            "type": "individual",
            "title": "title 1",
            "body": {"exercise 1": "10", "exercise 2": "10", "exercise 3": "10"},
            "user_id": user_id,
            "date_created": "2024-04-01T18:00:00.000000",
        },
    )
