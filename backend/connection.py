import motor.motor_asyncio
import os
from dotenv import load_dotenv
load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get('MONGO_URI'))
if client:
    print("Connection to MongoDB successful")
else:
    print("Failed to connect to MongoDB")
    
database = client.test_database
user_collection = database.users