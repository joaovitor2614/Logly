

from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from ..utils.security import get_current_user
from app.settings import APP_SETTINGS
from faker import Faker
from randomuser import RandomUser
import random


router = APIRouter()

@router.get("/", response_description="Get professors data in Database", status_code=status.HTTP_200_OK)
async def get_professors(request: Request, user_id: str = Depends(get_current_user)):
    professors_database = request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME]
    professors = list(professors_database.find(limit=100))
    for professor in professors:
        professor["_id"] = str(professor["_id"])
    return professors

@router.post("/test/{amount}", response_description="Post fake professors data in Database", status_code=status.HTTP_200_OK)
async def create_fake_professors(request: Request, amount: int, user_id: str = Depends(get_current_user)):
    professors_database =  request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME]
    fake = Faker()
    user_list = RandomUser.generate_users(amount)
    for user in user_list:

        new_professor = {
            "name": fake.name(),''
            "image": user.get_picture(),
            "disciplines": [fake.job(), fake.job()],
            "gender": user.get_gender(),
            "email":  user.get_email(),
            "phone": user.get_phone(),
            "upvotes": random.randint(0, 10),
            "downvotes": random.randint(0, 10)
        }
        new_professor = jsonable_encoder(new_professor)
        new_professor = professors_database.insert_one(new_professor)



    
    