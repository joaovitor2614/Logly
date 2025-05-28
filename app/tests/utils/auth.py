from fastapi import Response
from fastapi.testclient import TestClient





class AuthEndPointMocker:
    def __init__(self, client):
        self.client = client

    def register(self, user_data: dict):
        response = self.client.post(
            "/auth/register",
            json=user_data,
        )
        return response
