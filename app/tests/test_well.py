from app.tests.utils.wrapper.well import WellEndPointWrapper
from app.controllers.well import WellController

from app.settings import APP_SETTINGS


def test_import_well_file(client, import_well_file):
    response = import_well_file

    assert response.status_code == 201
    
    well_controller = WellController(client)
    well_db_obj = well_controller.get_well_by_name("WELL1")

  
    assert well_db_obj is not None, "Failed to import well file"
    assert len(well_db_obj["welllogs"]) == 20, "Well logs were not imported sucessfully"
    




