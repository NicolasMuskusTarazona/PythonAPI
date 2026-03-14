# fast api
from fastapi import APIRouter, Response, status
# database mongodb
from config.db import conn
# GET BY ID and GET ALL
from schemas.user import userEntity,usersEntity
# MODEL USER
from models.user import User
# CRYPT PASSWORD USERS
from passlib.hash import sha256_crypt
# EASY METHOD ( GET BY ID , DELETE and PUT)
from bson import ObjectId
# HTTP STATUS
from starlette.status import *

user = APIRouter()

# GET ALL
@user.get('/users', response_model=list[User], tags=["users"])
def get_all_users():
    return usersEntity(conn.local.user.find())


# GET BY ID
@user.get('/users/{id}', response_model= User, tags=["users"])
def get_id_users(id:str):
    return userEntity(conn.local.user.find_one({"_id": ObjectId (id)}))


# POST
@user.post('/users', response_model=User, tags=["users"])
def post_users(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    id = conn.local.user.insert_one(new_user).inserted_id

    user_created = conn.local.user.find_one({"_id": id})

    return userEntity(user_created)


# PUT
@user.put('/users/{id}',response_model= User, tags=["users"])
def put_users(id:str, user: User):
    conn.local.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))

# DELETE
@user.delete('/users/{id}', status_code=HTTP_204_NO_CONTENT, tags=["users"])
def delete_users(id: str):
    userEntity(conn.local.user.find_one_and_delete({"_id": ObjectId (id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)