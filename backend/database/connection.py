from pymongo.mongo_client import MongoClient
import os

class MongoConnection:
    def __init__(self):
        self.mongo_uri = os.environ.get("MONGO_URI")
        if not self.mongo_uri:
            raise ValueError("MONGO_URI environment variable not set")
        self.client = self.connect_to_database()

    def connect_to_database(self):
        try:
            client = MongoClient(self.mongo_uri)
            client.server_info()
            return client
        except ConnectionError as e:
            print(f"Error connecting to database: {e}")
            raise

    def get_database(self):
        return self.client.get_database()

    def get_collection(self, collection: str):
        return self.get_database()[collection]

    def drop_collection(self, collection):
        self.get_database().drop_collection(collection)

    def seed_collection(self, collection, data):
        self.get_database()[collection].insert_many(data)
