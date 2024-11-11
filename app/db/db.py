import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
database = client.get_database('user_db')

def get_database():
    """
    Returns the database instance. This can be imported and used
    in other files to interact with the MongoDB database.
    """
    return database

