from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("No MONGO_URI found in environment variables")

conn = MongoClient(MONGO_URI)
db = conn.get_default_database()