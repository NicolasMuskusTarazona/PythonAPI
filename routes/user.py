# fast api
from fastapi import APIRouter, Response, status, HTTPException, Depends
# database mongodb
from config.db import db
# GET BY ID and GET ALL
from schemas.user import userEntity, usersEntity
# MODEL USER
from models.user import User
# CRYPT PASSWORD USERS
from passlib.hash import sha256_crypt
# EASY METHOD ( GET BY ID , DELETE and PUT)
from bson import ObjectId
# HTTP STATUS
from starlette.status import *
# Auth dependencies
from dependencies.auth import get_current_admin

user = APIRouter()

# GET ALL 
@user.get('/users', response_model=list[User], tags=["users"])
def get_all_users(current_user: dict = Depends(get_current_admin)):
    return usersEntity(db.user.find())

# GET BY ID 
@user.get('/users/{id}', response_model=User, tags=["users"])
def get_id_users(id: str, current_user: dict = Depends(get_current_admin)):
    return userEntity(db.user.find_one({"_id": ObjectId(id)}))

# POST (CREA LA CUENTA)
@user.post('/users', response_model=User, tags=["users"])
def post_users(user: User):
    existing_user = db.user.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = dict(user)
    new_user["password"] = sha256_crypt.hash(new_user["password"])  # hash seguro
    new_user["role"] = "user"

    try:
        id = db.user.insert_one(new_user).inserted_id
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error creating user")

    user_created = db.user.find_one({"_id": id})
    return userEntity(user_created)


# PUT 
@user.put('/users/{id}', response_model=User, tags=["users"])
def put_users(id: str, user: User, current_user: dict = Depends(get_current_admin)):
    db.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return userEntity(db.user.find_one({"_id": ObjectId(id)}))

# DELETE
@user.delete('/users/{id}', status_code=HTTP_204_NO_CONTENT, tags=["users"])
def delete_users(id: str, current_user: dict = Depends(get_current_admin)):
    userEntity(db.user.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)