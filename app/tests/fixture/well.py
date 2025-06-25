from app.tests.utils.test_data_path import TEST_WELL_FILE_PATH

from app.tests.utils.wrapper.well import WellEndPointWrapper
import pytest

@pytest.fixture
def import_well_file(client, register_user):
        
    _, request_headers  = register_user
    well_endpoint_mocker = WellEndPointWrapper(client, request_headers)
  
    response = well_endpoint_mocker.import_file(TEST_WELL_FILE_PATH)

    return response, request_headers