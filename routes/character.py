# fast api
from fastapi import APIRouter, Response, status, HTTPException
# database mongodb
from config.db import conn
# GET BY ID and GET ALL
from schemas.character import characterEntity,charactersEntity
# MODEL Characters
from models.character import Character
# EASY METHOD ( GET BY ID , DELETE and PUT)
from bson import ObjectId
# HTTP STATUS
from starlette.status import *

character = APIRouter()

# GET ALL
@character.get('/characters', response_model=list[Character], tags=["characters"])
def get_all_characters():
    return charactersEntity(conn.local.character.find())

# GET BY ID
@character.get('/characters/{id}', response_model= Character, tags=["characters"])
def get_id_characters(id:str):
    return characterEntity(conn.local.character.find_one({"_id": ObjectId (id)}))

# POST
@character.post('/characters', response_model=Character, tags=["characters"])
def post_characters(character: Character):
    new_character = dict(character)
    id = conn.local.character.insert_one(new_character).inserted_id

    character_created = conn.local.character.find_one({"_id": id})
    return characterEntity(character_created)

# PUT
@character.put('/characters/{id}',response_model= Character, tags=["characters"])
def put_characters(id:str, characters: Character):
    put_character=conn.local.character.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(characters)})
    # NOT FOUND CHARACTER
    if put_character is None:
        raise HTTPException(status_code=404,detail="Character not found")
    return characterEntity(conn.local.character.find_one({"_id": ObjectId(id)}))

from fastapi import status

# DELETE
@character.delete('/characters/{id}', status_code=status.HTTP_200_OK, tags=["characters"])
def delete_characters(id: str):
    deleted_character = conn.local.character.find_one_and_delete({"_id": ObjectId(id)})
    # NOT FOUND CHARACTER
    if deleted_character is None:
        raise HTTPException(status_code=404,detail="Character not found")
    return {"message": "Character deleted successful!"}