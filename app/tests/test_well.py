from app.tests.utils.wrapper.well import WellEndPointWrapper
from app.controllers.well import WellController
from app.controllers.welldata import WellDataController
from app.tests.utils.test_data_path import TEST_WELL_FILE_PATH
from app.tests.utils.auth import get_user_id_from_request_headers
from app.settings import APP_SETTINGS


def test_import_well_file(client, register_user):

    _, request_headers  = register_user
    well_controller = WellController(client)
    well_data_controller = WellDataController(client)
    well_endpoint_wrapper = WellEndPointWrapper(client, request_headers)
    response = well_endpoint_wrapper.import_file(TEST_WELL_FILE_PATH)


    assert response.status_code == 201
    

    well_db_obj = well_controller.get_well_by_name("WELL1")
    well_id = well_db_obj["_id"]
    well_data_db_objs = well_data_controller.get_all_well_log_data_db_objs_by_well_id(well_id)
  
    assert well_db_obj is not None, "Failed to import well file"
    assert len(well_data_db_objs) == 20
    assert len(well_db_obj["welllogs"]) == 20, "Well logs were not imported sucessfully"
    

def test_get_wells(client, import_well_file):
    request_headers = import_well_file
    well_endpoint_wrapper = WellEndPointWrapper(client, request_headers)
    response = well_endpoint_wrapper.get_wells()
    assert response.status_code == 201
    well_db_objs_jsonfied = response.json()

    assert len(well_db_objs_jsonfied) == 1


def test_delete_well(client, import_well_file):
    request_headers  = import_well_file
    well_endpoint_wrapper = WellEndPointWrapper(client, request_headers)
    well_controller = WellController(client)

    user_id = get_user_id_from_request_headers(request_headers)
    well_db_objs = well_controller.get_all_wells_data(user_id)


    response = well_endpoint_wrapper.delete_well(well_db_objs[0]["_id"])
    well_db_objs = well_controller.get_all_wells_data(user_id)
    assert response.status_code == 201
    assert len(well_db_objs) == 0

def test_get_well_log_data(client, import_well_file):
    request_headers  = import_well_file
    well_endpoint_wrapper = WellEndPointWrapper(client, request_headers)
    well_controller = WellController(client)

    user_id = get_user_id_from_request_headers(request_headers)
    well_db_obj = well_controller.get_all_wells_data(user_id)[0]
    well_log_db_objs = well_db_obj["welllogs"]
    response = well_endpoint_wrapper.get_well_log_data(well_log_db_objs[0]["_id"], well_db_obj["_id"])
    assert response.status_code == 201

    
    

