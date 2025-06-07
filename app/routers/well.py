import jwt
from fastapi import APIRouter, Request, Response, HTTPException, status
from app.models.well.well import ImportWell
from app.settings import APP_SETTINGS
from ..controllers.well import WellController


router = APIRouter()


@router.post("/", response_description="Register user in Database", status_code=status.HTTP_201_CREATED)
def import_well_file(request: Request, file_info: ImportWell):
    well_controller = WellController(request)
    print('file_info', file_info)
    well_controller.import_well(file_info.file_path)
    
