from bson import ObjectId

user_data = [
    {
        "_id": ObjectId("65fedb7a8433a888c1aca57c"),
        "name": "user1",
        "email": "user1@email.com",
        "workouts": [],
        "friends": ["75fedb7a8433a888c1aca57d", "95fedb7a8433a888c1aca57f"],
    },
    {
        "_id": ObjectId("75fedb7a8433a888c1aca57d"),
        "name": "user2",
        "email": "user2@email.com",
        "workouts": ["65fedb7a8433a888c1aca57a", "65fedb7a8433a888c1aca57b"],
        "friends": ["65fedb7a8433a888c1aca57c", "95fedb7a8433a888c1aca57f"],
    },
    {
        "_id": ObjectId("85fedb7a8433a888c1aca57e"),
        "name": "user3",
        "email": "user3@email.com",
        "workouts": ["65fedb7a8433a888c1aca57c"],
        "friends": [],
    },
    {
        "_id": ObjectId("95fedb7a8433a888c1aca57f"),
        "name": "user4",
        "email": "user4@email.com",
        "workouts": [],
        "friends": ["65fedb7a8433a888c1aca57c", "75fedb7a8433a888c1aca57d"],
    },
]
