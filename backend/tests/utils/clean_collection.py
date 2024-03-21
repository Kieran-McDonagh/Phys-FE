from backend.database.connection import MongoConnection
from backend.tests.seed_test_data.users import users as user_data


class CleanTestDatabase:
    def __init__(self):
        self.connection = MongoConnection()

    def clean_user_collection(self):
        self.connection.drop_collection("test_users")
        self.connection.seed_collection("test_users", user_data)
