from fastapi import Request, status, HTTPException
from app.models.well.well import WellLogData
from app.settings import APP_SETTINGS
from .base import BaseController
from typing import List
import uuid
import json


class WellDataController(BaseController):
    def __init__(self, request: Request):
         self.well_database =  request.app.database[APP_SETTINGS.WELLS_DATA_DB_NAME]
         super().__init__(self.well_database)
    def _serialize_well_log_data_numpy_array(self, well_log_data: list):    
        print('type', type(well_log_data))     
        return json.dumps(well_log_data)
    def delete_all_well_data_by_well_id(self, well_id: str | uuid.UUID):
        if isinstance(well_id, uuid.UUID):
            well_id = str(well_id)
        self.well_database.delete_many({"well_id": well_id})

    def delete_well_data_by_well_log_id(self, well_log_id: str | uuid.UUID):
        if isinstance(well_log_id, uuid.UUID):
            well_log_id = str(well_log_id)
        self.well_database.delete_one({"well_log_id": well_log_id})

    def _create_well_logs_data_db_objs(self, 
        well_logs_info, 
        well_id,
        well_log_data_db_objs_ids
    ) -> List[WellLogData]:
        return [
            WellLogData(
                well_id=well_id,
                well_log_id=str(well_log_data_db_objs_ids[i]),
                data=well_log_info["data"],
            ) 
            for (i, well_log_info) in enumerate(well_logs_info)
        ]
    def get_all_well_log_data_db_objs_by_well_id(self, well_id):
    
        well_log_data_db_objs = list(self.well_database.find({"well_id": well_id}))
        return well_log_data_db_objs
    def get_well_log_data_by_id(self, well_id: str, well_log_id: str):
        well_log_data_db_obj = self.well_database.find_one({"well_id": well_id, "well_log_id": well_log_id})
        if well_log_data_db_obj is None:
            HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Well log data not found!")
            return
        well_log_data_serialized = self._serialize_well_log_data_numpy_array(well_log_data_db_obj["data"])
        return well_log_data_serialized
        
  

        
