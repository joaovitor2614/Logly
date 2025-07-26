from app.tests.utils.wrapper.well import WellEndPointWrapper
from app.controllers.well import WellController
from app.tests.utils.test_data_path import TEST_WELL_FILE_PATH
from app.tests.utils.auth import get_user_id_from_register_response
from app.settings import APP_SETTINGS


def test_import_well_file(client, import_well_file):
    response, _ = import_well_file

    assert response.status_code == 201
    
    well_controller = WellController(client)
    well_db_obj = well_controller.get_well_by_name("WELL1")

  
    assert well_db_obj is not None, "Failed to import well file"
    assert len(well_db_obj["welllogs"]) == 20, "Well logs were not imported sucessfully"
    

def test_get_wells(client, import_well_file):
    _, request_headers = import_well_file
    well_endpoint_wrapper = WellEndPointWrapper(client, request_headers)
    response = well_endpoint_wrapper.get_wells()
    assert response.status_code == 201
    well_db_objs_jsonfied = response.json()

    assert len(well_db_objs_jsonfied) == 1


def test_delete_well(client, register_user):
    mock_new_user_data, request_headers  = register_user
    well_endpoint_wrapper = WellEndPointWrapper(client, request_headers)
    well_controller = WellController(client)
    well_endpoint_wrapper.import_file(TEST_WELL_FILE_PATH)
    user_id = mock_new_user_data["_id"]
    well_db_objs = well_controller.get_all_wells_data(user_id)


    response = well_endpoint_wrapper.delete_well(well_db_objs[0]["_id"])
    well_db_objs = well_controller.get_all_wells_data(user_id)
    assert response.status_code == 201
    assert len(well_db_objs) == 0

    
    #user_id = get_user_id_from_register_response(response)

    #well_controller = WellController(client)

    #well_id = well_controller.get_well_by_name("WELL1")["_id"]

    #well_endpoint_wrapper.delete_well(well_id)
    #assert response.status_code == 201

    #wells_db_objs = well_controller.get_all_wells_data(user_id)
    #assert len(wells_db_objs) == 0

    


