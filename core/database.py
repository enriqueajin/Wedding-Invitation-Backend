from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv 

load_dotenv()

# Create a new client and connect to the server
client = MongoClient(os.getenv('MONGODB_URL'), server_api=ServerApi('1'))

# Get database
db = client.wedding

# Get collection
attendance_collection = db["attendance"]