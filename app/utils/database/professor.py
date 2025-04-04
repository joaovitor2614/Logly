

from typing import Literal
from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends, File, UploadFile
from ...models.professor.professor import Professor, UpVote, DownVote
from fastapi.encoders import jsonable_encoder

from bson.objectid import ObjectId
from app.settings import APP_SETTINGS



def get_professor_by_id(request: Request, professor_id: str):
    
    """
    Get professor by id.

    Args:
        request (Request): The request object.
        professor_id (str): The id of the professor.

    Returns:
        Professor: The professor object.

    Raises:
        HTTPException: If the professor is not found.
    """


    professors_database = request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME]
    professor = professors_database.find_one(
        {"_id": ObjectId(professor_id)}    
    )
  
    if not professor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Professor not found!"
        )
        return None
    return professor
def retrive_rank_updated_professor(
        request: Request, 
        professor: Professor, 
        user_id: ObjectId, 
        feedback_type: Literal["upvotes", "downvotes"] = "upvotes"
    ):
    professors_database = request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME]
    professor = add_feedback_to_professor(professor, user_id, feedback_type)
    new_professor_votes = jsonable_encoder(professor[feedback_type])
    update_result = professors_database.update_one(
            {"_id": professor["_id"]}, {"$set": {feedback_type: new_professor_votes}}
    )
    

    professor = professors_database.find_one(
        {"_id":  professor["_id"]}    
    )
    professor["_id"] = str(professor["_id"])
    return professor

def add_feedback_to_professor(professor: Professor, user_id: ObjectId, feedback_type: Literal["upvotes", "downvotes"] = "upvotes"):
    
    
    if not professor or not user_id:
        print('Professor object and user id must be provided.')
        return
    has_user_feedbacked_professor = any(feedback["user_id"] == user_id for feedback in professor[feedback_type])
    if has_user_feedbacked_professor:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"User already {'upvoted' if feedback_type == 'upvotes' else 'downvoted'} professor!"
        ) 
    feedback_object = UpVote(user_id=user_id) if feedback_type == "upvotes" else DownVote(user_id=user_id)
    professor[feedback_type].append(feedback_object) #professor["upvotes"].
    return professor

