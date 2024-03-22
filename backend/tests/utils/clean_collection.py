from backend.database.connection import MongoConnection
from backend.tests.seed_test_data.users import users


class CleanTestDatabase:
    def __init__(self):
        self.connection = MongoConnection()

    def clean_user_collection(self):
        self.connection.drop_collection("test_users")
        return self

    def seed_user_collection(self):
        self.connection.seed_collection("test_users", users)
        return self
