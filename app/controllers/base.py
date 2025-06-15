from fastapi import Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from app.settings import APP_SETTINGS

from bson.objectid import ObjectId
from pydantic import BaseModel



class BaseController:
    def __init__(self, database):
        self.database = database

    def add_new_db_obj(self, db_obj: BaseModel):
        db_json_jsonfied = jsonable_encoder(db_obj)
        new_db_obj = self.database.insert_one(db_json_jsonfied)
        return new_db_obj.inserted_id
