

from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends, File, UploadFile
from fastapi.encoders import jsonable_encoder
from ..utils.security import get_current_user
from ..utils.picture import save_picture
from ..utils.database.update import update_document_object_instance
from ..models.professor.professor import Professor, Comment, UpVote, DownVote
from ..controllers.professor import ProfessorController
from bson.objectid import ObjectId
from app.settings import APP_SETTINGS
from faker import Faker
from randomuser import RandomUser
from datetime import datetime
import random


router = APIRouter()

@router.post("/", response_description="Add a professor in Database", status_code=status.HTTP_201_CREATED)
def create_professor(request: Request, new_professor: Professor, user_id: str = Depends(get_current_user)):
    professor_controller = ProfessorController(request)
    created_new_professor = professor_controller.add_professor(new_professor, True)
    return created_new_professor


    
    
@router.get("/", response_description="Get professors data in Database", status_code=status.HTTP_200_OK)
async def get_professors(request: Request, user_id: str = Depends(get_current_user)):
    professor_controller = ProfessorController(request)
    professors_db = professor_controller.get_professors()
    return professors_db

@router.get("/{id}", response_description="Get professor by id data in Database", status_code=status.HTTP_200_OK)
async def get_professor_by_id(id: str, request: Request, user_id: str = Depends(get_current_user)):
    professor_controller = ProfessorController(request)
    professor_db = professor_controller.get_professor_db_instance_by_id(id)
    return professor_db


@router.put("/{id}", response_description="Update a professor", response_model=Professor, )
def update_professor(id: str, request: Request, professor: Professor = Body(...), user_id: str = Depends(get_current_user)):
    professors_database = request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME]
    professor_data = _data.dict(exclude_unset=True)
    updated_professor = update_document_object_instance(professors_database, id, professor_data)

    return updated_professor
@router.put("/upvotes/{id}", response_description="Upvote a professor", status_code=status.HTTP_201_CREATED)
def up_vote_professor(id: str, request: Request, response: Response,  user_id: str = Depends(get_current_user)):
    professor_controller = ProfessorController(request)
    updated_professor = professor_controller.handle_professor_feedback(id, user_id, "upvotes")
    return updated_professor

@router.put("/downvotes/{id}", response_description="Downvote a professor", status_code=status.HTTP_201_CREATED)
def down_vote_professor(id: str, request: Request, response: Response,  user_id: str = Depends(get_current_user)):
    professor_controller = ProfessorController(request)
    updated_professor = professor_controller.handle_professor_feedback(id, user_id, "downvotes")
    return updated_professor



@router.put("/comments/{id}", response_description="Comment a professor", status_code=status.HTTP_201_CREATED)
def add_professor_comment(id: str, request: Request, comment: Comment,  user_id: str = Depends(get_current_user)):
    professor_controller = ProfessorController(request)
    professor = professor_controller.add_professor_comment(id, user_id, comment)
    return professor

@router.delete("/comments/{id}/{comment_id}", response_description="Comment a professor", status_code=status.HTTP_201_CREATED)
def remove_professor_comment(id: str, comment_id: str, request: Request, user_id: str = Depends(get_current_user)):
    professor_controller = ProfessorController(request)
    professor = professor_controller.remove_professor_comment(id, user_id, comment_id)
    return professor

@router.delete("/{id}", response_description="Delete a professors")
def delete_professor(id: str, request: Request, response: Response,  user_id: str = Depends(get_current_user)):
    delete_result = request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME].delete_one({"_id": (ObjectId(id))})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Professor with ID {id} not found")

@router.post("/test/{amount}", response_description="Post fake professors data in Database", status_code=status.HTTP_200_OK)
async def create_fake_professors(request: Request, amount: int, user_id: str = Depends(get_current_user)):
    professor_controller = ProfessorController(request)
    professor_controller.add_fake_professors(amount)

    
    