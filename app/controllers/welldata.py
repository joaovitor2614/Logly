from fastapi import Request
from bson.objectid import ObjectId
from app.models.well.well import WellLog, WellLogData
from app.settings import APP_SETTINGS
from .base import BaseController
from typing import List
import uuid

class WellDataController(BaseController):
    def __init__(self, request: Request):
         self.well_database =  request.app.database[APP_SETTINGS.WELLS_DATA_DB_NAME]
         super().__init__(self.well_database)

    def _create_well_logs_data_db_objs(
        self, 
        well_logs_info: List[dict], 
        well_log_data_db_objs_ids: List[uuid.UUID]
    ) -> List[WellLog]:
        return [
            WellLogData(
                well_log_id=str(well_log_data_db_objs_ids[i]),
                data=well_log_info["data"],
            ) 
            for (i, well_log_info) in enumerate(well_logs_info)
        ]
    
    def get_well_log_data_by_id(self, well_log_id: str):
        well_log_id = ObjectId(well_log_id)
        print('get_well_log_data_by_id')

        
