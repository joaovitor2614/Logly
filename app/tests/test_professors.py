from app.tests.utils.token import get_authorization_setted_request_headers_from_register_response
from ..models.professor.professor import Professor
from bson.objectid import ObjectId
from app.routers import ENDPOINTS
from app.settings import APP_SETTINGS
import pytest
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
    #response = client.post(f"{ENDPOINTS.PROFESSORS}/test/3", headers=request_headers)
    get_professors_response = client.get(f"{ENDPOINTS.PROFESSORS}", headers=request_headers)

    fetched_professors = get_professors_response.json()

    professor_model_fields = list(Professor.model_fields.keys())


    assert get_professors_response.status_code == 200
    assert len(fetched_professors) == FAKE_PROFESSORS_AMOUNT, "Get professors failed"
    for professor in fetched_professors:
        for professor_field in professor_model_fields:
            assert professor_field in professor, f"{professor_field} not in professor"

@pytest.mark.parametrize("feedback_type", ["upvotes", "downvotes"])
def test_feedback_professor(feedback_type, client, register_user):
    response, _ = register_user
    request_headers = get_authorization_setted_request_headers_from_register_response(response)

    get_professors_response = client.get(f"{ENDPOINTS.PROFESSORS}", headers=request_headers)
    fetched_professors = get_professors_response.json()
 
    professor_id = fetched_professors[0]["_id"]
    voted_professor_response = client.put(f"{ENDPOINTS.PROFESSORS}/{feedback_type}/{professor_id}", headers=request_headers)
    #updated_feedback_professor_db_obj = voted_professor_response.json()
    #assert len(updated_feedback_professor_db_obj[feedback_type]) == 1
    
    #print('upvote_professor_response', upvote_professor_response)
    #assert upvote_professor_response.status_code == 200

    # Get upvotes professor
    #upvoted_professor = client.get(f"{ENDPOINTS.PROFESSORS}/{professor_id}", headers=request_headers)
    #print('upvoted_professor', upvoted_professor)


def test_comment_professor(client, register_user):
    response, _ = register_user
    request_headers = get_authorization_setted_request_headers_from_register_response(response)
    #response = client.post(f"{ENDPOINTS.PROFESSORS}/test/{FAKE_PROFESSORS_AMOUNT}", headers=request_headers)
    get_professors_response = client.get(f"{ENDPOINTS.PROFESSORS}", headers=request_headers)
    fetched_professors = get_professors_response.json()
    print('fetched_professors', fetched_professors)
    professor_id = fetched_professors[0]["_id"]

    comment_text = "test comment"

    comment_professor_response = client.post(
        "f{ENDPOINTS.PROFESSORS}/comments/{professor_id}", headers=request_headers, json={"comment": comment_text}
    )
    assert comment_professor_response.status_code == 200




      
