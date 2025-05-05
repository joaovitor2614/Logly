from fastapi import Request, HTTPException, status
from app.models.professor.professor import Professor, UpVote, DownVote, Comment
from fastapi.encoders import jsonable_encoder
from app.settings import APP_SETTINGS
from bson.objectid import ObjectId
from faker import Faker
from typing import Union, Literal, List
from randomuser import RandomUser
import random

class ProfessorController:
    def __init__(self, request: Request):
         self.professor_database =  request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME]

    def _create_fake_professor(self, faker_instance):
        return Professor(
                name=faker_instance.name(),
                image=faker_instance.image_url(),
                disciplines=['Calculo IV'],
                gender='other',
                email=faker_instance.email(),
                phone=faker_instance.phone_number()
            )        

    def _remove_professor_feedback_for_user(
        self,
        professor: Professor, 
        user_id: str, 
        feedback_type: Literal["upvotes", "downvotes"] = "upvotes"
    ) -> Professor:
        professor[feedback_type].remove({"user_id": user_id})
        return professor

    def __add_professor_feedback_for_user(
       self,
       professor: Professor, 
       user_id: str, 
       feedback_type: Literal["upvotes", "downvotes"] = "upvotes"
    ) -> Professor:
        feedback_object = UpVote(user_id=user_id) if feedback_type == "upvotes" else DownVote(user_id=user_id)
        professor[feedback_type].append(feedback_object) #professor["upvotes"].
        return professor

    def _add_professor_to_db(self, professor: Professor, return_db_obj: bool = False) -> Union[None, Professor]:
        professor = jsonable_encoder(professor)
        new_professor = self.professor_database.insert_one(professor)
        if return_db_obj:
            created_new_professor = self.professor_database.find_one(
                {"_id": new_professor.inserted_id}
            )
            created_new_professor["_id"] = str(created_new_professor["_id"])
            return created_new_professor

    def _update_professor_obj_field(self, professor_id: str, field_name: str, field_value: list):
        print('field_value', field_value)
        field_value_json_encoded = jsonable_encoder(field_value)

        self.professor_database.update_one(
            {"_id": ObjectId(professor_id)}, {"$set": {field_name: field_value_json_encoded}}
        )




    def handle_professor_feedback(
        self, professor_id: str, user_id: str, feedback_type: Literal["upvotes", "downvotes"] = "upvotes"
        ) -> Professor:
        
        professor_db_obj = self.get_professor_db_instance_by_id(professor_id)
        print('professor_db_instance', professor_db_obj, professor_id)
        if not professor_db_obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Professor not found")

        has_user_feedbacked_professor = any(feedback["user_id"] == user_id for feedback in professor_db_obj[feedback_type])
        print('has_user_feedbacked_professor', has_user_feedbacked_professor)
        if has_user_feedbacked_professor:
            professor_db_obj = self._remove_professor_feedback_for_user(professor_db_obj, user_id, feedback_type)
        else:
            professor_db_obj = self.__add_professor_feedback_for_user(professor_db_obj, user_id, feedback_type)
        self._update_professor_obj_field(professor_id, feedback_type, professor_db_obj[feedback_type])
        new_professor_data = self.get_professor_db_instance_by_id(professor_id)
        new_professor_data["_id"] = str(new_professor_data["_id"])
        return new_professor_data
        
    def get_professor_db_instance_by_id(self, id: str):

        professor = self.professor_database.find_one({"_id": ObjectId(id)})
        professor["_id"] = str(professor["_id"])
        return professor

    def get_professors(self) -> List[Professor]:
        
        professors = list(self.professor_database.find())
        for professor in professors:
            professor["_id"] = str(professor["_id"])
        return professors

    def add_fake_professors(self, amount: int):
        fake = Faker()
        fake_professor_db_instances = [self._create_fake_professor(fake) for _ in range(amount)]

        for fake_professor_db_instance in fake_professor_db_instances:
            self._add_professor_to_db(fake_professor_db_instance)

    def add_professor(self, professor: Professor) -> Professor:
         self._add_professor_to_db(fake_professor_db_instance)

    def add_professor_comment(self, professor_id: str, user_id: str, new_comment: Comment) -> Professor:
        professor_db_instance = self.get_professor_db_instance_by_id(professor_id)
        all_profs = self.get_professors()
        print('professor_db_instance', professor_id, 'all profs', all_profs)

        if not professor_db_instance:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Professor not found")
        new_comment.user_id = str(user_id)

        professor_db_instance["comments"].append(new_comment)

        self._update_professor_obj_field(professor_id, "comments", professor_db_instance["comments"])
        new_professor_data = self.get_professor_db_instance_by_id(professor_id)
        new_professor_data["_id"] = str(new_professor_data["_id"])
        return new_professor_data

    def remove_professor_comment(self, professor_id: str, user_id: str, comment_id: str):
        professor_db_instance = self.get_professor_db_instance_by_id(professor_id)
        professor_comment = next(
            (comment for comment in professor_db_instance["comments"] if comment.get('_id') == comment_id), 
            None
        )
        if not professor_comment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
        if professor_comment.user_id != str(user_id):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

        professor_db_instance["comments"].remove(professor_comment)
        self._update_professor_obj_field(professor_id, "comments", professor_db_instance["comments"])
        new_professor_data = self.get_professor_db_instance_by_id(professor_id)
        new_professor_data["_id"] = str(new_professor_data["_id"])
        return new_professor_data



           

  