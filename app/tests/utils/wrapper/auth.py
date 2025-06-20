from fastapi import Response
from fastapi.testclient import TestClient
from app.utils.security import decode_jwt_token, verify_password


def get_user_id_from_register_response(response: Response) -> str:
    token = response.json()["token"]
    jwt_payload = decode_jwt_token(token)
    user_id = jwt_payload["data"]["id"]
    return user_id

class AuthEndPointWrapper:

    def __init__(self, client, request_headers=None):
        self.client = client
        self.request_headers = request_headers

    def register(self, user_data: dict):
        response = self.client.post(
            "/auth/register",
            json=user_data,
        )
        return response

    def login(self, email: str, password: str):
        response = self.client.post(
            "/auth/login",
            json={"email": email, "password": password},
        )
        return response


