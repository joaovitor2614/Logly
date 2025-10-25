from fastapi import Request
from bson.objectid import ObjectId
from fastapi import Request, HTTPException, status
from app.database import mongo_db
from app.models.well.well import WellLog, WellLogData, Well
from app.core.well import well_handler
from app.settings import APP_SETTINGS
from .base import BaseController
from .welldata import WellDataController
from bson.objectid import ObjectId
from typing import List
import json

DEPTH_WELL_LOG_MNEMONICS = ["DEPTH", "MD"]

class WellController(BaseController):
    def __init__(self, request: Request):
        """
        Initialize the WellController object.

        Args:
            request (Request): The current request instance.

        Sets the following instance variables:
            self.well_database: The database collection for wells.
            self.well_data_database: An instance of WellDataController for managing well log data.
        """

        
        self.well_database =  mongo_db[APP_SETTINGS.WELLS_DB_NAME]
        self.well_data_database = WellDataController(request)
        super().__init__(self.well_database)

    def _create_well_logs_db_objs(self, well_logs_info: List[dict]) -> List[WellLog]:
     
        """
        Create a list of WellLog objects from a list of dictionaries containing well log information.

        Args:
            well_logs_info (List[dict]): A list of dictionaries containing well log information.

        Returns:
            List[WellLog]: A list of WellLog objects.
        """
        return [
            WellLog(
                name=well_log_info["mnemonic"],
                unit=well_log_info["unit"],
                description=well_log_info["descr"],
            ) 
            for well_log_info in well_logs_info
        ]
    


    def _create_well_db_obj(self, well_info: dict, user_id: ObjectId, well_logs_db_objs: List[WellLog]):
        """
        Create a Well object from the given well information and well log objects.

        Args:
            well_info (dict): A dictionary containing well information.
            user_id (ObjectId): The user ID to associate with the well.
            well_logs_db_objs (List[WellLog]): A list of WellLog objects.

        Returns:
            Well: A Well object.
        """
        return Well(
            name=well_info["name"],
            start=well_info["start"],
            stop=well_info["stop"],
            company=well_info["company"],
            user_id=user_id,
            welllogs=well_logs_db_objs
        )
    
    def get_wells_amount_for_user(self, user_id: str):
        return self.well_database.count_documents({"user_id": user_id})
        

    def get_well_by_name(self, well_name: str):
        """
        Retrieve a well by its name.

        Args:
            well_name (str): The name of the well to retrieve.

        Returns:
            Well: The well object if found, None otherwise.
        """
        return self.well_database.find_one(
            {"name": well_name}    
        )
    
    def get_well_by_id(self, well_id: str | ObjectId):
        """
        Retrieve a well by its ID.

        Args:
            well_id (str | ObjectId): The ID of the well to retrieve.

        Returns:
            Well: The well object if found, None otherwise.
        """
        return self.well_database.find_one({"_id": well_id})
    
    def get_depth_well_log_id(self, well_id: str):
        well_db_obj = self.get_well_by_id(well_id)
        depth_well_log_id = None
        for well_log_db_obj in well_db_obj["welllogs"]:
            if well_log_db_obj["name"].strip().upper() in DEPTH_WELL_LOG_MNEMONICS:
                depth_well_log_id = well_log_db_obj["_id"]
                break

        if depth_well_log_id is None:
            raise HTTPException(status_code=404, detail="Depth well log not found")
        return depth_well_log_id
    

    def import_well(self, *,las_file_object,user_id: ObjectId):


        """
        Import a well from a LAS file and save it to the database.

        Args:
            las_file_object (UploadFile): The LAS file to import.
            user_id (ObjectId): The ID of the user who is importing the well.

        Returns:
            None
        """

        
        try:

            well_info = well_handler.get_well_info_from_las_file(las_file_object)
        except Exception as e:  
            raise HTTPException(status_code=400, detail=f"Error importing well: {e}")
            
        well_log_db_objs = self._create_well_logs_db_objs(well_info["well_logs"])
        well_db_obj = self._create_well_db_obj(well_info, user_id, well_log_db_objs)
        
        well_log_db_objs_ids = [well_log_db_obj.id for well_log_db_obj in well_log_db_objs]

        well_log_data_db_objs = self.well_data_database._create_well_logs_data_db_objs(well_info["well_logs"], str(well_db_obj.id),well_log_db_objs_ids)
        
        self.save_well_related_db_objs(well_db_obj, well_log_data_db_objs)

    def save_well_related_db_objs(self, well_db_obj: Well, well_log_data_db_objs: List[WellLogData]):
        well_db_inserted_id = self.add_new_db_obj(well_db_obj)
        for well_log_data_db_obj in well_log_data_db_objs:
            well_log_data_db_obj.data = json.dumps(well_log_data_db_obj.data)
            self.well_data_database.add_new_db_obj(well_log_data_db_obj)
        

    def get_all_wells_data(self, user_id: str):
        well_db_objs = list(self.well_database.find({"user_id": user_id}))
            
        return well_db_objs
    
    def update_well_field(self, well_id: str, field_name: str, new_field_value):
        """
        Update a field in the well database.

        Args:
            well_id (str): The ID of the well to update.
            field_name (str): The name of the field to update.
            new_field_value (any): The new value for the field.
        """
        self.well_database.update_one(
            {"_id": well_id}, {"$set": {field_name: new_field_value}}
        )
    
    def delete_well_by_id(self, well_id: str | ObjectId):
        self.well_data_database.delete_all_well_data_by_well_id(well_id)
        self.well_database.delete_one({"_id": well_id})

    def delete_well_log_by_ids(self, well_id: str | ObjectId, well_log_id: str | ObjectId):
        """
        Delete a well log from a well by their IDs.

        Args:
            well_id (str | ObjectId): The ID of the well.
            well_log_id (str | ObjectId): The ID of the well log to delete.

        Returns:
            None
        """
        
        self.well_data_database.delete_well_data_by_well_log_id(well_log_id)
        well_db_obj = self.get_well_by_id(well_id)
        for well_log_db_obj in well_db_obj["welllogs"]:
    
            if well_log_db_obj["_id"] == well_log_id:
                well_log_to_remove_index = well_db_obj["welllogs"].index(well_log_db_obj)
                break

        well_db_obj["welllogs"].pop(well_log_to_remove_index)
        well_db_obj["welllogs"]
     
        self.update_well_field(well_id, "welllogs", well_db_obj["welllogs"])


    def delete_all_wells_by_user_id(self, user_id: str | ObjectId):
        """
        Delete all wells associated with a given user ID from the database.

        Args:
            user_id (str | ObjectId): The ID of the user whose wells to delete.

        Returns:
            None
        """
        self.well_database.delete_many({"user_id": user_id})


                
        
