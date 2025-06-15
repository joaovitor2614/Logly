from app.tests.utils.well import WellEndPointMocker
from app.settings import APP_SETTINGS


def test_import_well_file(client, register_user):
    _, request_headers  = register_user
    well_endpoint_mocker = WellEndPointMocker(client, request_headers)
    las_file_path = "C:\\Users\\jvito\\Desktop\\Projects\\logly\\app\\tests\\data\\well1.las"
    well_endpoint_mocker.import_file(las_file_path)

    
    #well_db_mock = client.app.database[APP_SETTINGS.WELLS_DB_NAME]
    #new_well = well_db_mock.find_one(
    #    {"name": "WELL1"}    
    #)
    #print('new_well', new_well)
    #assert new_well is not None, "Failed to import well file"
    ##assert len(new_well.welllogs) == 19, "Well logs were not imported sucessfully"
    




