import jwt
from fastapi import APIRouter, Request, UploadFile, status, Depends, File, HTTPException
from ..utils.security import get_current_user
from bson.objectid import ObjectId
from app.settings import APP_SETTINGS
from app.core.well import well_handler
from ..controllers.well import WellController
from ..controllers.welldata import WellDataController
import io
router = APIRouter()

MAX_WELLS_PER_USER = 3

@router.post("/basic_info", response_description="Get Las File Basic Info", status_code=status.HTTP_201_CREATED)
def get_las_file_basic_info(
    request: Request,  
    las_file: UploadFile = File(...), 
    user_id: ObjectId = Depends(get_current_user) 
    ):
    """
    Get the basic information of the LAS file.

    Args:
        request (Request): FastAPI request.
        las_file (UploadFile): The LAS file to get the basic information from.
        user_id (ObjectId): The ID of the user who is importing the well.

    Returns:
        None
    """
    print('get_las_file_basic_info')
    basic_well_info = well_handler.get_basic_info_from_las_file_object(las_file)


@router.post("/", response_description="Import Well Las Info", status_code=status.HTTP_201_CREATED)
def import_well_file(
    request: Request,  
    las_file: UploadFile = File(...), 
    user_id: ObjectId = Depends(get_current_user) 
    ):

    well_controller = WellController(request)
    
    user_wells_amount = well_controller.get_wells_amount_for_user(user_id)
    if user_wells_amount >= MAX_WELLS_PER_USER:
        raise HTTPException(status_code=400, detail="You have reached the maximum number of wells per user.")

  
    well_controller.import_well(
        las_file_object=las_file,
        user_id=user_id
    )

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

@router.delete("/data/{well_id}/{well_log_id}", response_description="Remove by well log by ids", status_code=status.HTTP_201_CREATED)
def delete_well_log(request: Request, well_id: str, well_log_id: str, user_id: ObjectId = Depends(get_current_user)):
    well_controller = WellController(request)
  
    well_controller.delete_well_log_by_ids(well_id, well_log_id)
  





@router.get("/data/{well_id}/{well_log_id}", response_description="Get well log data by ID", status_code=status.HTTP_201_CREATED)
def get_well_log_data_by_id(request: Request, well_log_id: str, well_id: str,user_id: ObjectId = Depends(get_current_user)):
    well_log_data_controller = WellDataController(request)
  
    well_log_data = well_log_data_controller.get_well_log_data_by_id(well_id, well_log_id)
   
    return {"data": well_log_data}