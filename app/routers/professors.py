

from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends, File, UploadFile
from fastapi.encoders import jsonable_encoder
from ..utils.security import get_current_user
from ..utils.professor import create_new_fake_professors
from ..utils.picture import save_picture
from ..utils.database.professor import get_professor_by_id, add_feedback_to_professor, retrive_rank_updated_professor
from ..models.professor.professor import Professor, Comment, UpVote, DownVote
from bson.objectid import ObjectId
from app.settings import APP_SETTINGS
from faker import Faker
from randomuser import RandomUser
from datetime import datetime
import random


router = APIRouter()
base = '/users/'
UploadImage = f'{base}image-upload'

@router.post("/upload", response_description="Upload professor image", status_code=status.HTTP_201_CREATED)
def upload_professor_image(file: UploadFile = File(...)):
    imageUrl = save_picture(file=file, folderName='professors', fileName='myfile')
    print('imageUrl', imageUrl)
    return {"imageUrl": imageUrl}

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


@router.get("/{id}", response_description="Get professor data by ID", status_code=status.HTTP_200_OK)
async def get_professor_by_id(request: Request, user_id: str = Depends(get_current_user)):
    professor = get_professor_by_id(request, id)

    return professor

@router.put("/{id}", response_description="Update a professor", response_model=Professor, )
def update_professor(id: str, request: Request, professor: Professor = Body(...), user_id: str = Depends(get_current_user)):
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
@router.put("/upvotes/{id}", response_description="Upvote a professor", status_code=status.HTTP_201_CREATED)
def up_vote_professor(id: str, request: Request, response: Response,  user_id: str = Depends(get_current_user)):
    #professors_database = request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME]
    professor = get_professor_by_id(request, id)

    feedback_type = "upvotes"

    update_ranks_professor = retrive_rank_updated_professor(request, professor, user_id, feedback_type)

    #update_ranks_professor = add_feedback_to_professor(professor, user_id, feedback_type)

    return update_ranks_professor

@router.put("/downvotes/{id}", response_description="Downvote a professor", status_code=status.HTTP_201_CREATED)
def down_vote_professor(id: str, request: Request, response: Response,  user_id: str = Depends(get_current_user)):
    professors_database = request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME]
    professor = get_professor_by_id(request, id)

    feedback_type = "downvotes"
    update_ranks_professor = retrive_rank_updated_professor(request, professor, user_id, feedback_type)
    #update_ranks_professor = add_feedback_to_professor(professor, user_id, feedback_type)

    return update_ranks_professor

@router.put("/comments/{id}", response_description="Comment a professor", status_code=status.HTTP_201_CREATED)
def add_professor_comment(id: str, request: Request, comment: Comment,  user_id: str = Depends(get_current_user)):
    professors_database = request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME]
    users_database = request.app.database[APP_SETTINGS.USERS_DB_NAME]
    professor = get_professor_by_id(request, id)

    user = users_database.find_one(
        {"_id": user_id}    
    )
    comment.user_id = str(user_id)
    comment.author = user["name"]

    professor["comments"].append(comment)
    new_professor_comments = jsonable_encoder(professor["comments"])
    update_result = professors_database.update_one(
            {"_id": professor["_id"]}, {"$set": {"comments": new_professor_comments}}
    )

    professor = professors_database.find_one(
        {"_id":  professor["_id"]}    
    )
    professor["_id"] = str(professor["_id"])
    return professor

    #update_ranks_professor = add_feedback_to_professor(professor, user_id, feedback_type)

    return update_ranks_professor
@router.delete("/{id}", response_description="Delete a professors")
def delete_professor(id: str, request: Request, response: Response,  user_id: str = Depends(get_current_user)):
    delete_result = request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME].delete_one({"_id": (ObjectId(id))})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Professor with ID {id} not found")

@router.post("/test/{amount}", response_description="Post fake professors data in Database", status_code=status.HTTP_200_OK)
async def create_fake_professors(request: Request, amount: int, user_id: str = Depends(get_current_user)):
    professors_database =  request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME]


    new_fake_professors = create_new_fake_professors(amount)
    for new_fake_professor in new_fake_professors:
        new_fake_professor = jsonable_encoder(new_fake_professor)
        new_fake_professor = professors_database.insert_one(new_fake_professor)

    
    