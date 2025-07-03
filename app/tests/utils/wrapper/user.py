from fastapi import Response
from fastapi.testclient import TestClient




class UserEndPointWrapper:

    def __init__(self, client, request_headers=None):

        self.client = client
        self.request_headers = request_headers

    def get_users(self):
        response = self.client.get(
            "/users",
            headers=self.request_headers
        )
        return response

    def send_verification_code(self):
        response = self.client.post(
            "/users/send-verification-code",
            headers=self.request_headers
        )
        return response

