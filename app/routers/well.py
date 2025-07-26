import jwt
from fastapi import APIRouter, Request, Response, HTTPException, status, Depends
from app.models.well.well import ImportWell
from ..utils.security import get_current_user
from bson.objectid import ObjectId
from app.settings import APP_SETTINGS
from ..controllers.well import WellController
from ..controllers.welldata import WellDataController

router = APIRouter()


@router.post("/", response_description="Register user in Database", status_code=status.HTTP_201_CREATED)
def import_well_file(request: Request, file_info: ImportWell, user_id: ObjectId  = Depends(get_current_user)):

    well_controller = WellController(request)
    
    well_controller.import_well(file_info.file_path, user_id)

    return {"message": "Well imported successfully"}
    

@router.get("/", response_description="Get all imported wells data", status_code=status.HTTP_201_CREATED)
def get_all_wells_data(request: Request, user_id: ObjectId = Depends(get_current_user)):
    well_controller = WellController(request)
  
    well_db_obs = well_controller.get_all_wells_data(user_id)
   
    return well_db_obs

@router.delete("/{well_id}", response_description="Remove by well by id", status_code=status.HTTP_201_CREATED)
def delete_well(request: Request, well_id: str, user_id: ObjectId = Depends(get_current_user)):
    well_controller = WellController(request)
  
    well_db_obs = well_controller.delete_well_by_id(well_id)
    return well_db_obs




@router.get("/data/{well_log_id}", response_description="Get well log data by ID", status_code=status.HTTP_201_CREATED)
def get_well_log_data_by_id(request: Request, well_log_id: str, user_id: ObjectId = Depends(get_current_user)):
    well_log_data_controller = WellDataController(request)
  
    well_log_data = well_log_data_controller.get_well_log_data_by_id(well_log_id)
   
    return {"data": well_log_data}