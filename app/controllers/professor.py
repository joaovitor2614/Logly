from fastapi import Request, HTTPException, status
from ...models.professor.professor import Professor, UpVote, DownVote
from app.settings import APP_SETTINGS
import random

class ProfessorController:
    def __init__(request: Request):
         self.professor_database =  request.app.database[APP_SETTINGS.PROFESSORS_DB_NAME]

    def _create_fake_professor_instances_from_obj(self, fake_professor_obj):
        return Professor(
                name='Armando',
                image=fake_professor_obj.get_picture(),
                disciplines=['Calculo IV'],
                gender=fake_professor_obj.get_gender(),
                email=fake_professor_obj.get_email(),
            )        

    def _remove_professor_feedback_for_user(
        self,
        professor: Professor, 
        user_id: ObjectId, 
        feedback_type: Literal["upvotes", "downvotes"] = "upvotes"
    ) -> Professor:
        professor[feedback_type].remove({"user_id": user_id})
        return professor

    def __add_professor_feedback_for_user(
       self,
       professor: Professor, 
       user_id: ObjectId, 
       feedback_type: Literal["upvotes", "downvotes"] = "upvotes"
    ) -> Professor:
        feedback_object = UpVote(user_id=user_id) if feedback_type == "upvotes" else DownVote(user_id=user_id)
        professor[feedback_type].append(feedback_object) #professor["upvotes"].
        return professor

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

    def add_fake_professors(self, amount: int):
        fake_professors_objs = RandomUser.generate_users(amount)
        fake_professor_db_instances = [
            self._create_fake_professor_instances_from_obj(fake_professors_obj) 
            for fake_professors_obj in fake_professors_objs
        ]
        for fake_professor_db_instance in fake_professor_db_instances:
            fake_professor_db_instances = jsonable_encoder(fake_professor_db_instances)
            self.professor_database.insert_one(fake_professor_db_instances)


  