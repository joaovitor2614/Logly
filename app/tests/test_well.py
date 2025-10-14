from app.tests.utils.wrapper.well import WellEndPointWrapper
from app.controllers.well import WellController
from app.controllers.welldata import WellDataController
from app.tests.utils.test_data_path import TEST_WELL_FILE_PATH
from app.tests.utils.auth import get_user_id_from_request_headers
import pytest


class TestWell:
    @pytest.fixture(autouse=True)
    def setup(self, client, register_user):
        self.client = client
        _, request_headers  = register_user
        self.well_controller = WellController(client)
        self.well_data_controller = WellDataController(client)
        self.well_endpoint_wrapper = WellEndPointWrapper(client, request_headers)
        self.user_id = get_user_id_from_request_headers(request_headers)

    def test_import_well_file(self):
        response = self.well_endpoint_wrapper.import_file(TEST_WELL_FILE_PATH)


        assert response.status_code == 201
        
        well_db_obj = self.well_controller.get_well_by_name("WELL1")
        well_id = well_db_obj["_id"]
        well_data_db_objs = self.well_data_controller.get_all_well_log_data_db_objs_by_well_id(well_id)
    
        assert well_db_obj is not None, "Failed to import well file"
        assert len(well_data_db_objs) == 20
        assert len(well_db_obj["welllogs"]) == 20, "Well logs were not imported sucessfully"

    def test_get_wells(self, import_well_file):

  
        response = self.well_endpoint_wrapper.get_wells()
        assert response.status_code == 201
        well_db_objs_jsonfied = response.json()

        assert len(well_db_objs_jsonfied) == 1

    def test_delete_well(self, import_well_file):
        well_db_objs = self.well_controller.get_all_wells_data(self.user_id)


        response = self.well_endpoint_wrapper.delete_well(well_db_objs[0]["_id"])
        well_db_objs = self.well_controller.get_all_wells_data(self.user_id)
        assert response.status_code == 201
        assert len(well_db_objs) == 0
    
    def test_delete_well_log_id(self, import_well_file):
        well_db_objs = self.well_controller.get_all_wells_data(self.user_id)

        well_id = well_db_objs[0]["_id"]
        well_log_to_delete_name = "GR"
        
        well_log_info = next((d for d in well_db_objs[0]["welllogs"] if d["name"] == well_log_to_delete_name), None)
    
        response = self.well_endpoint_wrapper.delete_well_log_by_ids(well_db_objs[0]["_id"], well_log_info["_id"])
        assert response.status_code == 201

        well_db_objs = self.well_controller.get_all_wells_data(self.user_id)
        well_logs_info = well_db_objs[0]["welllogs"]
    
        assert any(well_log_db_obj["name"] == well_log_to_delete_name for well_log_db_obj in well_logs_info) == False

        
    def test_get_well_log_data(self, import_well_file):


        well_db_obj = self.well_controller.get_all_wells_data(self.user_id)[0]
        well_log_db_objs = well_db_obj["welllogs"]
        response = self.well_endpoint_wrapper.get_well_log_data(well_log_db_objs[0]["_id"], well_db_obj["_id"])
        assert response.status_code == 201



    def test_get_basic_well_info_from_las_file(self):
        response = self.well_endpoint_wrapper.get_basic_well_info_from_las_file(TEST_WELL_FILE_PATH)
        assert response.status_code == 201

        




    
    

