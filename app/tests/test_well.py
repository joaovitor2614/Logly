from app.tests.utils.well import WellEndPointMocker



def test_import_well_file(client, register_user):
    _, request_headers  = register_user
    well_endpoint_mocker = WellEndPointMocker(client, request_headers)
    well_endpoint_mocker.import_file("./data/well1.las")

