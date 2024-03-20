import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()


class MongoConnection:
    testing = os.environ.get("ENV") == "test"
    
    def __init__(self):
        self.mongo_uri = os.environ.get("MONGO_URI")
        self.test_mongo_uri = os.environ.get("TEST_MONGO_URI")
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.get_mongo_uri())
        self.database = self.client.get_database()
        print("connected to:", self.database.name)

    def get_mongo_uri(self):
        if self.testing:
            print("In test environment")
            return self.test_mongo_uri
        else:
            print("In production environment")
            return self.mongo_uri

    def get_collection(self, collection):
        if self.testing:
            print(f"connecting to test_{collection} collection")
            return self.database.get_collection(f"test_{collection}")
        else:
            print(f"connecting to {collection} collection")
            return self.database.get_collection(collection)

    async def drop_collection(self, collection):
        try:
            await self.database.drop_collection(collection)
            print(f"Dropped collection: {collection}")
        except Exception as e:
            print("Error dropping collection:", e)

    async def seed_collection(self, collection, data):
        try:
            await self.database[collection].insert_many(data)
            print(f"seeded collection: {collection}")
        except Exception as e:
            print("Error seeding collection:", e)
