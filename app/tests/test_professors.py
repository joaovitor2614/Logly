from app.tests.utils.token import get_authorization_setted_request_headers_from_register_response
from app.routers import ENDPOINTS


def test_generate_fake_professors(client, register_user):

    response, _ = register_user

    request_headers = get_authorization_setted_request_headers_from_register_response(response)
    fake_professors_amount = 3
    response = client.post(f"{ENDPOINTS.PROFESSORS}/test/{fake_professors_amount}", headers=request_headers)
    assert response.status_code == 200

   


def test_get_professors(client, register_user):
    response, _ = register_user

    request_headers = get_authorization_setted_request_headers_from_register_response(response)
    fake_professors_amount = 2
    response = client.post(f"{ENDPOINTS.PROFESSORS}/test/{fake_professors_amount}", headers=request_headers)

    get_professors_response = client.get(f"{ENDPOINTS.PROFESSORS}", headers=request_headers)
    assert get_professors_response.status_code == 200
