from fastapi import Request, HTTPException, status
from app.models.user.user import UserCreate
from fastapi.encoders import jsonable_encoder
from ..utils.security import get_hashed_password, verify_password
from app.core.well import WellHandler
from .user import UserController
from app.settings import APP_SETTINGS
from .base import BaseController
from bson.objectid import ObjectId

class WellController(BaseController):
    def __init__(self, request: Request):
         self.well_database =  request.app.database[APP_SETTINGS.WELLS_DB_NAME]
         super().__init__(self.well_database)


    def import_well(self, las_file_path: str, user_id: str):
        well_handler = WellHandler(las_file_path, user_id)
        well_db_obj = well_handler.get_well_db_obj_from_las_file()
        print('well_db_obj', well_db_obj)
        self.add_new_db_obj(well_db_obj)

    def get_all_wells_data(self, user_id: str):
        well_db_objs = self.well_database.find({"user_id": ObjectId(user_id)})
        return well_db_objs

        
