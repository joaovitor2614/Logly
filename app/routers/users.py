import jwt
from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends
from ..models.user import UserCreate, UserCrendentials
from fastapi.encoders import jsonable_encoder
from ..utils.security import get_current_user
from bson.objectid import ObjectId
from app.settings import APP_SETTINGS


router = APIRouter()


@router.get("/", response_description="Get user info in Database", status_code=status.HTTP_200_OK)
async def get_user(request: Request, user_id: str = Depends(get_current_user)):
    database =  request.app.database[APP_SETTINGS.DB_NAME]
    print('user_id', user_id, type(user_id))

    user = database.find_one(
        {"_id":  ObjectId(user_id)}    
    )
  
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found!"
        )
    return {"id": user_id, "name": user["name"], "email": user["email"]}
