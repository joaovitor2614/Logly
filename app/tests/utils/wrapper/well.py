from fastapi import Response
from fastapi.testclient import TestClient





class WellEndPointWrapper:
    def __init__(self, client, request_headers):
        self.client = client
        self.request_headers = request_headers

    def import_file(self, las_file_path: str):
        response = self.client.post(
            "/well",
            headers=self.request_headers,
            json={"file_path": las_file_path},
        )
        return response

    def get_wells(self):
        response = self.client.get(
            "/well",
            headers=self.request_headers,
        )
        return response