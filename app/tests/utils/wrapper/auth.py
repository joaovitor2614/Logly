from fastapi import Response






class AuthEndPointWrapper:

    def __init__(self, client):
        self.client = client

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


