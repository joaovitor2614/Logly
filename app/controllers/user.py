from fastapi import Request, HTTPException, status
from app.models.user.user import UserCreate
from fastapi.encoders import jsonable_encoder
from ..utils.security import get_hashed_password, verify_password
from app.settings import APP_SETTINGS
from .base import BaseController
from libgravatar import Gravatar
from faker import Faker
from bson.objectid import ObjectId
from typing import Union, Literal, List
import random
from datetime import timedelta

class UserController(BaseController):
    def __init__(self, request: Request):
         self.user_database =  request.app.database[APP_SETTINGS.USERS_DB_NAME]
         super().__init__(self.user_database)

    def get_user_by_id(self, id: str) -> UserCreate:
        user = self.user_database.find_one(
            {"_id": id}

        )
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User not found!"
            )

        return user

    def get_user_by_email(self, email: str):
        user = self.user_database.find_one(
            {"email": email}
        )
        '''
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with given email not found!"
            )
            return
        '''
        return user
    def create_user(self, user_data: UserCreate) -> dict:
        user = self.get_user_by_email(user_data.email)

        if user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User with given email already exists!"
            )

        g = Gravatar(user_data.email)
        setattr(user_data, "image", g.get_image())
        self.set_user_info_hashed_password(user_data)
        user_id = self.add_new_user_to_database(user_data)
        user_db_obj = self.get_user_by_id(user_id)
        return user_db_obj

    def add_new_user_to_database(self, user_data: UserCreate):
        return self.add_new_db_obj(user_data)


    def set_user_info_hashed_password(self, user_data: UserCreate):
        hashed_password = get_hashed_password(user_data.password)
        user_data.password = hashed_password

    def set_user_verification_code(self, user_obj: dict, otp_code: str):
        
        self.user_database.update_one(
            {"_id": user_obj["_id"]}, {"$set": {"verification_code": otp_code}}
        )

    def verify_verification_code(self, user_obj: dict, otp_code: str):
        if user_obj["verification_code"] != otp_code:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Verification code is not valid!"
            )
            return
        self.set_user_acccount_verified_status(user_obj)
        

    def set_user_acccount_verified_status(self, user_obj: dict):
        self.user_database.update_one(
            {"_id": user_obj["_id"]}, {"$set": {"has_confirmed_email": True}}
        )

     


    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        is_password_valid = verify_password(plain_password, hashed_password)
        if not is_password_valid:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Password is not valid!"
            )
    
