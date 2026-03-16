from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # carga variables de .env

MONGO_URI = os.getenv("MONGO_URI")
conn = MongoClient(MONGO_URI)