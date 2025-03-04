

from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from ..utils.security import get_current_user
from app.settings import APP_SETTINGS
from faker import Faker

router = APIRouter()


@router.post("/test/{amount}", response_description="Post fake professors data in Database", status_code=status.HTTP_200_OK)
async def get_user(request: Request, amount: int, user_id: str = Depends(get_current_user)):
    professors_database =  request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME]
    for _ in range(amount):
        fake = Faker()
        new_professor = {
            "name": fake.name(),
            "image": fake.image_url(),
            "disciplines": [fake.job(), fake.job()],
            "upvotes": 0,
            "downvotes": 0
        }
        new_professor = jsonable_encoder(new_professor)
        new_professor = professors_database.insert_one(new_professor)


    
    