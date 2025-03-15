

from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from ..utils.security import get_current_user
from ..models.professor import Professor
from bson.objectid import ObjectId
from app.settings import APP_SETTINGS
from faker import Faker
from randomuser import RandomUser
import random


router = APIRouter()

@router.post("/", response_description="Add a professor in Database", status_code=status.HTTP_201_CREATED)
def create_professor(request: Request, new_professor: Professor, user_id: str = Depends(get_current_user)):
    professors_database = request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME]
    professor = professors_database.find_one(
        {"name": new_professor.name}
    )
    if professor:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Professor with given name already exists!"
        )
    new_professor = jsonable_encoder(new_professor)
    new_professor = professors_database.insert_one(new_professor)
    created_new_professor = professors_database.find_one(
        {"_id": new_professor.inserted_id}
    )
    created_new_professor["_id"] = str(created_new_professor["_id"])
    return created_new_professor


    
    
@router.get("/", response_description="Get professors data in Database", status_code=status.HTTP_200_OK)
async def get_professors(request: Request, user_id: str = Depends(get_current_user)):
    professors_database = request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME]
    professors = list(professors_database.find())
    for professor in professors:
        professor["_id"] = str(professor["_id"])
    return professors

@router.put("/{id}", response_description="Update a professor", response_model=Professor, )
def update_book(id: str, request: Request, professor: Professor = Body(...), user_id: str = Depends(get_current_user)):
    professors_database = request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME]
    professor = {k: v for k, v in professor.dict().items() if v is not None}
    if len(professor) >= 1:
        update_result = professors_database.update_one(
            {"_id": ObjectId(id)}, {"$set": professor}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Professor with ID {id} not found")

    if (
        existing_professor := professors_database.find_one({"_id": ObjectId(id)})
    ) is not None:
        return existing_professor

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Professor with ID {id} not found")

@router.delete("/{id}", response_description="Delete a professors")
def delete_book(id: str, request: Request, response: Response,  user_id: str = Depends(get_current_user)):
    delete_result = request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME].delete_one({"_id": (ObjectId(id))})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Professor with ID {id} not found")

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
            "email":  user.get_email(),
            "phone": user.get_phone(),
            "upvotes": random.randint(0, 10),
            "downvotes": random.randint(0, 10)
        }
        new_professor = jsonable_encoder(new_professor)
        new_professor = professors_database.insert_one(new_professor)



    
    