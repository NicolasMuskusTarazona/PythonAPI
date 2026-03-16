from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("No MONGO_URI found in environment variables")

conn = MongoClient(MONGO_URI)

try:
    db = conn.get_default_database()
    # solo para testear
    print("Conexion MongoDB OK. Colecciones:", db.list_collection_names())
except Exception as e:
    print("❌ Error al conectar MongoDB:", e)
    raise e