import jwt
from fastapi import APIRouter, Request, Response, HTTPException, status, Depends
from app.models.well.well import ImportWell
from ..utils.security import get_current_user
from bson.objectid import ObjectId
from app.settings import APP_SETTINGS
from ..controllers.well import WellController


router = APIRouter()


@router.post("/", response_description="Register user in Database", status_code=status.HTTP_201_CREATED)
def import_well_file(request: Request, file_info: ImportWell, user_id: ObjectId  = Depends(get_current_user)):
    print('heree')
    well_controller = WellController(request)
    
    well_controller.import_well(file_info.file_path, user_id)

    return {"message": "Well imported successfully"}
    

@router.get("/", response_description="Get all imported wells data", status_code=status.HTTP_201_CREATED)
def get_all_wells_data(request: Request, user_id: ObjectId = Depends(get_current_user)):
    well_controller = WellController(request)
  
    well_db_obs = well_controller.get_all_wells_data(user_id)
    return well_db_obs