import motor.motor_asyncio
import os
from dotenv import load_dotenv
load_dotenv()


class MongoConnection:
    def __init__(self):
        self.mongo_uri = os.environ.get('MONGO_URI')
        self.test_mongo_uri = os.environ.get('TEST_MONGO_URI')
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.get_mongo_uri())
        self.database = self.client.get_database()
        print('connected to:', self.database.name)

    def get_mongo_uri(self):
        if os.environ.get('ENV') == 'test':
            print('Entering test environment')
            return self.test_mongo_uri
        else:
            print('entering production environment')
            return self.mongo_uri

    def get_user_collection(self):
        print('connecting to user collection')
        return self.database.get_collection("users")
    
    async def drop_collection(self, collection):
        try:
            await self.database.drop_collection(collection)
            print('Dropped collection:', collection)
        except Exception as e:
            print('Error dropping collection:', e)
            
    async def seed_users(self, user_data):
        try:
            await self.database['users'].insert_many(user_data)
            print('User collection seeded')
        except Exception as e:
            print('Error seeding collection:', e)


mongo_connection = MongoConnection()
user_collection = mongo_connection.get_user_collection()

