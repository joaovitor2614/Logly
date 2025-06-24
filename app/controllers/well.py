from fastapi import Request
from bson.objectid import ObjectId
from app.models.well.well import WellLog
from app.core.well import WellHandler
from app.settings import APP_SETTINGS
from .base import BaseController
from bson.objectid import ObjectId
from typing import List
import pandas as pd

class WellController(BaseController):
    def __init__(self, request: Request):
         self.well_database =  request.app.database[APP_SETTINGS.WELLS_DB_NAME]
         super().__init__(self.well_database)

    def get_well_by_name(self, well_name: str):
        return self.well_database.find_one(
        {"name": well_name}    
        )

    def import_well(self, las_file_path: str, user_id: ObjectId):
        well_handler = WellHandler(las_file_path, user_id)
        well_db_obj = well_handler.get_well_db_obj_from_las_file()
        well_db_obj.welllogs = self._serialize_well_db_objs_numpy_arrays(well_db_obj.welllogs)
        well_db_inserted_id = self.add_new_db_obj(well_db_obj)

    def get_all_wells_data(self, user_id: str):
        well_db_objs = self.well_database.find({"user_id": user_id})
        print('well_db_objs', well_db_objs)
        for well_db_obj in well_db_objs:
            print('well_db_obj', well_db_obj)
            well_db_obj.welllogs = self._serialize_well_db_objs_numpy_arrays(well_db_obj["welllogs"])

        return well_db_objs

    def _serialize_well_db_objs_numpy_arrays(self, well_log_db_objs: List[WellLog]):
        json_serialize_well_logs_data = []
        for well_log_db_obj in well_log_db_objs:
            well_log_data = well_log_db_obj["data"] if isinstance(well_log_db_obj, dict) else well_log_db_obj.data
            json_serialize_well_logs_data.append(pd.Series(well_log_data).to_json(orient='values'))
   
