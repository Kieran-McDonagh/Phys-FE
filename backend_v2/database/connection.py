from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


class MongoConnection:
    connected = False

    def __init__(self):
        self.environment = os.environ.get("ENV")
        self.mongo_uri = os.environ.get("MONGO_URI")
        self.test_mongo_uri = os.environ.get("TEST_MONGO_URI")
        self.client = self.connect_to_database()

    def connect_to_database(self):
        try:
            # just for logging purposes
            if not MongoConnection.connected:
                if self.environment == "testing":
                    print("connecting to test database")
                else:
                    print("connecting to production database")
                MongoConnection.connected = True
            # actually connecting to test or prod here
            if self.environment == "testing":
                return MongoClient(self.test_mongo_uri)
            else:
                return MongoClient(self.mongo_uri)
        except ValueError as e:
            print(f"Error connecting to database: {e}")
            raise

    def get_database(self):
        return self.client.get_database()

    def get_collection(self, collection: str):
        return self.get_database()[collection]

    def drop_collection(self, collection):
        collection = self.get_database()[collection]
        collection.drop()

    def seed_collection(self, collection, data):
        collection = self.get_database()[collection]
        collection.insert_many(data)
