

from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends, File, UploadFile
from fastapi.encoders import jsonable_encoder

from ..utils.picture import save_picture



from app.settings import APP_SETTINGS

from datetime import datetime
import random


router = APIRouter()
base = '/users/'
UploadImage = f'{base}image-upload'

@router.post("/", response_description="Upload image", status_code=status.HTTP_201_CREATED)
def upload_image(file: UploadFile = File(...)):
 
    imageUrl = save_picture(file=file, folderName='images', fileName=file.filename)
    print('imageUrl', imageUrl)
    return {"imageUrl": imageUrl}