from fastapi import Response
from fastapi.testclient import TestClient
from bson.objectid import ObjectId




class WellEndPointWrapper:
    def __init__(self, client, request_headers):
        self.client = client
        self.request_headers = request_headers




    def import_file(self, las_file_path: str):
        with open(las_file_path, "rb") as f:
            files = {"las_file": ("test.las", f, "application/octet-stream")}
            data = {"well_name": "Test Well"}  
            response = self.client.post(
                "/well/",  
                headers=self.request_headers,
                files=files,
                data=data
            )
        return response

    def get_wells(self):
        response = self.client.get(
            "/well",
            headers=self.request_headers,
        )
        return response
    
    def delete_well(self, well_id: str | ObjectId):
        if isinstance(well_id, ObjectId):
            well_id = str(well_id)
        response = self.client.delete(
            f"/well/{well_id}",
            headers=self.request_headers,
        )
        return response
    
    def delete_well_log_by_ids(self, well_id: str | ObjectId, well_log_id: str | ObjectId):
        well_id = str(well_id)
        well_log_id = str(well_log_id)
        response = self.client.delete(
            f"/well/data/{well_id}/{well_log_id}",
            headers=self.request_headers,
        )
        return response
    
    def get_well_log_data(self, well_log_id: str, well_id: str):
        response = self.client.get(
            f"/well/data/{well_id}/{well_log_id}",
            headers=self.request_headers,
        )
        return response
        
        
