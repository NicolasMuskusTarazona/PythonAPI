from config.db import db
from passlib.hash import sha256_crypt

def create_admin():
    # Buscar admin por email en mydb
    admin = db.users.find_one({"email": "nicolasmuskus1@gmail.com"})
    
    if admin is None:
        admin_user = {
            "name": "Nicolas",
            "email": "nicolasmuskus1@gmail.com",
            "password": sha256_crypt.hash("admin123"),
            "role": "admin"
        }

        # Insertar en mydb, no en mydb
        db.users.insert_one(admin_user)
        print("Admin user created")
    else:
        print("Admin already exists.")