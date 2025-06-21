from app.tests.utils.well import WellEndPointMocker
from app.controllers.well import WellController
from app.tests.utils.test_data_path import TEST_WELL_FILE_PATH
from app.settings import APP_SETTINGS


def test_import_well_file(client, register_user):
    
    _, request_headers  = register_user
    well_endpoint_mocker = WellEndPointMocker(client, request_headers)
    print('TEST_WELL_FILE_PATH', TEST_WELL_FILE_PATH)
    response = well_endpoint_mocker.import_file(TEST_WELL_FILE_PATH)
    assert response.status_code == 201
    
    well_controller = WellController(client)
    well_db_obj = well_controller.get_well_by_name("WELL1")

  
    assert well_db_obj is not None, "Failed to import well file"
    assert len(well_db_obj["welllogs"]) == 20, "Well logs were not imported sucessfully"
    




