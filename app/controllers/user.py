from fastapi import Request, HTTPException, status
from app.models.user.user import UserCreate, OTPCode
from ..utils.security import get_hashed_password, verify_password
from app.controllers.well import WellController
from datetime import datetime, UTC, timedelta
from app.settings import APP_SETTINGS
from .base import BaseController
from libgravatar import Gravatar
from app.database import mongo_db


class UserController(BaseController):
    def __init__(self, request: Request):
         
         self.well_controller = WellController(request)
         self.user_database =  mongo_db[APP_SETTINGS.USERS_DB_NAME]
         super().__init__(self.user_database)

    def delete_user_account(self, id: str):
        self.get_user_by_id(id)
        self.well_controller.delete_all_wells_by_user_id(id)
        self.user_database.delete_one({"_id": id})


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

    def get_user_by_email(self, email: str) -> dict:
        user = self.user_database.find_one(
            {"email": email}
        )
        
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

    def update_user_field(self, user_id: str, field_name: str, new_field_value):
        self.user_database.update_one(
            {"_id": user_id}, {"$set": {field_name: new_field_value}}
        )

    def set_user_verification_code(self, user_obj: dict, otp_code: str, otp_code_type):
        exp_time = datetime.now(UTC) + timedelta(minutes=APP_SETTINGS.ACCOUNT_VERIFICATION_OTP_CODE_EXPIRE_MINUTES)
        user_db_otp_code_attr = "otp_code" if otp_code_type == "account_verification" else "reset_password_otp_code"
        self.update_user_field(user_obj["_id"], f"{user_db_otp_code_attr}.exp", exp_time)
        self.update_user_field(user_obj["_id"], f"{user_db_otp_code_attr}.code", otp_code)
        self.update_user_field(user_obj["_id"], f"{user_db_otp_code_attr}.user_id", user_obj["_id"])


    def verify_verification_code(self, user_obj: dict, otp_code: str):
        otp_code_obj = user_obj["otp_code"]
        if datetime.now() > otp_code_obj["exp"]:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Verification code is expired!"
            )
        if otp_code_obj["code"] != otp_code:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Verification code is not valid!"
            )

        self.set_user_acccount_verified_status(user_obj)
        

    def set_user_acccount_verified_status(self, user_obj: dict):
        self.update_user_field(user_obj["_id"], "has_confirmed_email", True)
     
    def verify_password(self, plain_password: str, hashed_password: str):
        is_password_valid = verify_password(plain_password, hashed_password)
        if not is_password_valid:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Password is not valid!"
            )
    
