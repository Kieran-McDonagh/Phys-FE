import motor.motor_asyncio
import os
from dotenv import load_dotenv
load_dotenv()

mongo_uri = os.environ.get('MONGO_URI')
test_mongo_uri = os.environ.get('TEST_MONGO_URI')

# Function to get the appropriate MongoDB URI based on the environment
def get_mongo_uri():
    if os.environ.get('ENV') == 'test':
        print('Entering test environment')
        return test_mongo_uri
    else:
        print('entering production environment')
        return mongo_uri

client = motor.motor_asyncio.AsyncIOMotorClient(get_mongo_uri())
print("Connection to MongoDB successful")

database = client.get_database()
print("Connected to database:", database.name)

user_collection = database.get_collection("users")

