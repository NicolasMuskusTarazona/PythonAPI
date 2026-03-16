from config.db import conn
from passlib.hash import sha256_crypt

def create_admin():
    # Buscar admin por email en mydb
    admin = conn.mydb.users.find_one({"email": "nicolasmuskus1@gmail.com"})
    
    if admin is None:
        admin_user = {
            "name": "Nicolas",
            "email": "nicolasmuskus1@gmail.com",
            "password": sha256_crypt.hash("admin123"),
            "role": "admin"
        }

        # Insertar en mydb, no en mydb
        conn.mydb.users.insert_one(admin_user)
        print("Admin user created")
    else:
        print("Admin already exists.")