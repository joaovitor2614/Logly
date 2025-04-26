import jwt
from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends
from ..models.user.user import UserCreate, UserUpdate, UserCrendentials
from fastapi.encoders import jsonable_encoder
from ..utils.security import get_current_user
from ..utils.database.update import update_document_object_instance
from bson.objectid import ObjectId
from app.settings import APP_SETTINGS


router = APIRouter()

@router.put("/{id}", response_description="Update a user", response_model=UserCreate)
def update_user(id: str, request: Request, user: UserUpdate = Body(...), user_id: str = Depends(get_current_user)):
    database =  request.app.database[APP_SETTINGS.USERS_DB_NAME]
    user_data = user.dict(exclude_unset=True)
    updated_user = update_document_object_instance(database, id, user_data)

    return updated_user


@router.get("/{id}", response_description="Get user info by id in Database", status_code=status.HTTP_200_OK)
async def get_user_by_id(id: str, request: Request, user_id: str = Depends(get_current_user)):
    database =  request.app.database[APP_SETTINGS.USERS_DB_NAME]
   

    user = database.find_one(
        {"_id": id}    
    )
  
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found!"
        )
    return user

@router.get("/", response_description="Get user info in Database", status_code=status.HTTP_200_OK)
async def get_user(request: Request, user_id: str = Depends(get_current_user)):
    database =  request.app.database[APP_SETTINGS.USERS_DB_NAME]
   

    user = database.find_one(
        {"_id": user_id}    
    )
  
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found!"
        )
    return user
