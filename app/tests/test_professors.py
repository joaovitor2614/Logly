from app.tests.utils.token import get_authorization_setted_request_headers_from_register_response
from ..models.professor.professor import Professor
from app.routers import ENDPOINTS
from app.settings import APP_SETTINGS

FAKE_PROFESSORS_AMOUNT = 3
def test_generate_fake_professors(client, register_user):

    """
    Test the creation of fake professors.

    This test ensures that the endpoint for generating fake professors
    works correctly. It registers a user, obtains authorization headers,
    and sends a POST request to create a specified amount of fake professors.
    The test then asserts that the response status code is 200 and verifies
    that the correct number of fake professors have been added to the database.
    """

    response, _ = register_user

    request_headers = get_authorization_setted_request_headers_from_register_response(response)

    response = client.post(f"{ENDPOINTS.PROFESSORS}/test/{FAKE_PROFESSORS_AMOUNT}", headers=request_headers)
    assert response.status_code == 200
    professors_db_mock = client.app.database[APP_SETTINGS.PROFESSORS_DB_NAME]

    professors = list(professors_db_mock.find())
    assert len(professors) == FAKE_PROFESSORS_AMOUNT, "Add fake professors failed"


   


def test_get_professors(client, register_user):
    response, _ = register_user
    request_headers = get_authorization_setted_request_headers_from_register_response(response)
    get_professors_response = client.get(f"{ENDPOINTS.PROFESSORS}", headers=request_headers)

    fetched_professors = get_professors_response.json()

    professor_model_fields = list(Professor.model_fields.keys())


    assert get_professors_response.status_code == 200
    assert get_professors_response.status_code == 200
    assert len(fetched_professors) == FAKE_PROFESSORS_AMOUNT, "Get professors failed"
    for professor in fetched_professors:
        for professor_field in professor_model_fields:
            assert professor_field in professor, f"{professor_field} not in professor"
      
