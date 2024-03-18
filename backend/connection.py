import motor.motor_asyncio
import os
from dotenv import load_dotenv
load_dotenv()

testing = os.environ.get('TEST_ENV', '').lower() == 'true'

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get('MONGO_URI'))

if testing:
    print("Connection to test MongoDB successful")
    user_collection = client['test_db']['users']
else:
    print("Connection to MongoDB successful")
    user_collection = client['prod_db']['users']