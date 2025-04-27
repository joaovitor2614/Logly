from fastapi import Request, HTTPException, status
from app.models.professor.professor import Professor, UpVote, DownVote
from fastapi.encoders import jsonable_encoder
from app.settings import APP_SETTINGS
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



    def handle_professor_feedback(self, professor_id: str, user_id: str, feedback_type: Literal["upvotes", "downvotes"] = "upvotes"):
        
        professor_db_instance = self.get_professor_db_instance_by_id(professor_id)
        if not professor_db_instance:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Professor not found")

        has_user_feedbacked_professor = any(feedback["user_id"] == user_id for feedback in professor[feedback_type])
        if has_user_feedbacked_professor:
            professor = self._remove_professor_feedback_for_user(professor, user_id, feedback_type)
        else:
            professor = self.__add_professor_feedback_for_user(professor, user_id, feedback_type)
        
    def get_professor_db_instance_by_id(self, id: str):
        return self.professor_database.find_one({"_id": id})

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


           

  