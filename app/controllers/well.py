from fastapi import Request, HTTPException, status
from app.models.user.user import UserCreate
from fastapi.encoders import jsonable_encoder
from ..utils.security import get_hashed_password, verify_password
from app.core.well import WellHandler
from app.settings import APP_SETTINGS


class WellController:
    def __init__(self, request: Request):
         self.user_database =  request.app.database[APP_SETTINGS.USERS_DB_NAME]


    def import_well(self, las_file_path: str):
        well_handler = WellHandler(las_file_path)
