from fastapi import APIRouter, HTTPException
from config.db import db
from passlib.hash import sha256_crypt
from utils.jwt_manager import create_access_token
from models.auth import LoginData

auth = APIRouter()

# ACCESO CUENTA
@auth.post("/login", tags=["auth"])
def login(data: LoginData):
    user = db.user.find_one({"email": data.email})
    
    if user is None or not sha256_crypt.verify(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({
        "id": str(user["_id"]),
        "role": user["role"]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }