from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
db = MongoClient(MONGO_URI)

db = db["mydb"]