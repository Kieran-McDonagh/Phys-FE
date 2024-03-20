from backend.database.connection import MongoConnection
from backend.tests.seed_test_data.users import users as user_data


class CleanDatabase:
    def __init__(self):
        self.connection = MongoConnection()

    async def clean_user_collection(self):
        await self.connection.drop_collection("test_users")
        await self.connection.seed_collection("test_users", user_data)
