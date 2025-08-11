from fastapi import Request
from bson.objectid import ObjectId
from app.models.well.well import WellLog, WellLogData, Well
from app.core.well import WellHandler
from app.settings import APP_SETTINGS
from .base import BaseController
from .welldata import WellDataController
from bson.objectid import ObjectId
from typing import List
import json


class WellController(BaseController):
    def __init__(self, request: Request):
         self.well_database =  request.app.database[APP_SETTINGS.WELLS_DB_NAME]
         self.well_data_database = WellDataController(request)
         super().__init__(self.well_database)

    def _create_well_logs_db_objs(self, well_logs_info: List[dict]) -> List[WellLog]:
     
        return [
            WellLog(
                name=well_log_info["mnemonic"],
                unit=well_log_info["unit"],
                description=well_log_info["descr"],
            ) 
            for well_log_info in well_logs_info
        ]
    


    def _create_well_db_obj(self, well_info: dict, user_id: ObjectId, well_logs_db_objs: List[WellLog]):
        return Well(
            name=well_info["name"],
            user_id=str(user_id),
            welllogs=well_logs_db_objs
        )
        

    def get_well_by_name(self, well_name: str):
        return self.well_database.find_one(
        {"name": well_name}    
        )

    def import_well(self, *, well_name: str, las_file_object,user_id: ObjectId):
        well_handler = WellHandler()
        
        
        well_info = well_handler.get_well_info_from_las_file(las_file_object)



            
        


        well_log_db_objs = self._create_well_logs_db_objs(well_info["well_logs"])
        well_db_obj = self._create_well_db_obj(well_info, user_id, well_log_db_objs)
        
        well_log_db_objs_ids = [well_log_db_obj.id for well_log_db_obj in well_log_db_objs]
        print('well_log_db_objs_ids', well_log_db_objs_ids)
        print('well_info["well_logs"]', well_info["well_logs"])
        well_log_data_db_objs = self.well_data_database._create_well_logs_data_db_objs(well_info["well_logs"], str(well_db_obj.id),well_log_db_objs_ids)
        
        self.save_well_related_db_objs(well_db_obj, well_log_data_db_objs)

    def save_well_related_db_objs(self, well_db_obj: Well, well_log_data_db_objs: List[WellLogData]):
        well_db_inserted_id = self.add_new_db_obj(well_db_obj)
        for well_log_data_db_obj in well_log_data_db_objs:
            well_log_data_db_obj.data = json.dumps(well_log_data_db_obj.data)
            self.well_data_database.add_new_db_obj(well_log_data_db_obj)
        

    def get_all_wells_data(self, user_id: str):
        well_db_objs = list(self.well_database.find({"user_id": user_id}))

        for well_db_obj in well_db_objs:
            well_db_obj["_id"] = str(well_db_obj["_id"])
            
   

        return well_db_objs
    
    def delete_well_by_id(self, well_id: str | ObjectId):
        if isinstance(well_id, ObjectId):
            well_id = str(well_id)
        self.well_data_database.delete_all_well_data_by_well_id(well_id)
        self.well_database.delete_one({"_id": well_id})

    def delete_all_wells_by_user_id(self, user_id: str | ObjectId):
        if isinstance(user_id, ObjectId):
            user_id = str(user_id)
        self.well_database.delete_many({"user_id": user_id})


                
        
