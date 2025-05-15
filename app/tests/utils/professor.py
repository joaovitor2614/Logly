from fastapi import Request
from app.routers import ENDPOINTS
from fastapi.testclient import TestClient


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

