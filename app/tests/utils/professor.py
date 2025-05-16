from app.models.professor.professor import Professor
from fastapi import Request, Response
from app.routers import ENDPOINTS
from fastapi.testclient import TestClient


FAKE_PROFESSORS_AMOUNT = 3
class ProfessorClientMocker:
     def __init__(self, client: TestClient, request_headers: dict) -> None:
          self.client = client
          self.request_headers = request_headers

     def post_professor(self, professor_instance: Professor) -> Response:
          response = self.client.post(
               f"{ENDPOINTS.PROFESSORS}", 
               json=professor_instance.model_dump(mode='json'), 
               headers=self.request_headers
          )
          return response


     def generate_and_fetch_fake_professor(self):
          self.post_fake_professors()
          fetched_fake_professor = self.get_all_professors().json()
          return fetched_fake_professor
     def post_fake_professors(self) -> Response:
          response = self.client.post(f"{ENDPOINTS.PROFESSORS}/test/{FAKE_PROFESSORS_AMOUNT}", headers=self.request_headers) 
          return response
     def put_professor_feedback(self, professor_id: str, feedback_type: str) -> Response:
          response = self.client.put(f"{ENDPOINTS.PROFESSORS}/{feedback_type}/{professor_id}", headers=self.request_headers)
          return response     
     def get_all_professors(self) -> Response:
          response = self.client.get(f"{ENDPOINTS.PROFESSORS}", headers=self.request_headers)
          return response

     def get_professor_by_id(self, professor_id: str) -> Response:
          response = self.client.get(f"{ENDPOINTS.PROFESSORS}/{professor_id}", headers=self.request_headers)
          return response

     def get_current_user_id(self):
          response = self.client.get(f"{ENDPOINTS.USERS}", headers=self.request_headers)
          current_user = response.json()
          return current_user["_id"]

     def post_professor_comment(self, professor_id: str) -> Response:
          comment_text = "test comment"
          response = self.client.put(
               f"{ENDPOINTS.PROFESSORS}/comments/{professor_id}", headers=self.request_headers, json={"text": comment_text}
          )

          return response


def execute_generate_fake_profs_endpoint(client: TestClient, amount: str, request_headers: dict) -> Request:
     response = client.post(f"{ENDPOINTS.PROFESSORS}/test/{amount}", headers=request_headers)
     return response

def execute_get_all_professor_endpoint(client: TestClient, request_headers: dict) -> Request:
     response = client.get(f"{ENDPOINTS.PROFESSORS}", headers=request_headers)

     return response

def execute_add_professor_comment_endpoint(client: TestClient, request_headers: dict, professor_id: str) -> Request:
     comment_text = "test comment"
     response = client.put(
        f"{ENDPOINTS.PROFESSORS}/comments/{professor_id}", headers=request_headers, json={"text": comment_text}
     )

     return response

