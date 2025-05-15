
from ..models.professor.professor import Professor
from bson.objectid import ObjectId
from app.routers import ENDPOINTS
from app.settings import APP_SETTINGS
from app.controllers.professor import ProfessorController
from app.tests.utils.professor import ProfessorClientMocker, FAKE_PROFESSORS_AMOUNT, execute_generate_fake_profs_endpoint, execute_get_all_professor_endpoint, execute_add_professor_comment_endpoint
from app.utils.professor import create_new_fake_professor
import pytest

def test_generate_fake_professors(client, register_user):

    """
    Test the creation of fake professors.

    This test ensures that the endpoint for generating fake professors
    works correctly. It registers a user, obtains authorization headers,
    and sends a POST request to create a specified amount of fake professors.
    The test then asserts that the response status code is 200 and verifies
    that the correct number of fake professors have been added to the database.
    """
    
    response, _, request_headers = register_user
    professor_controller = ProfessorController(client)
    professor_client_mocker = ProfessorClientMocker(client, request_headers)

    # Execute the endpoint
    response = professor_client_mocker.post_fake_professors()
    assert response.status_code == 200

    # Query mongodb mock to check if fake fake professors were added

    professors = professor_controller.get_professors()
    assert len(professors) == FAKE_PROFESSORS_AMOUNT, "Add fake professors failed"


   
def test_add_new_professor(client, register_user):
    response, _, request_headers = register_user

    professor_controller = ProfessorController(client)
    professor_client_mocker = ProfessorClientMocker(client, request_headers)

    fake_professor_info = create_new_fake_professor()

    post_professor_response = professor_client_mocker.post_professor(fake_professor_info)
    

    assert post_professor_response.status_code == 201

    added_professor_id = str(post_professor_response.json()["_id"])
    added_professor_db_obj = professor_controller.get_professor_by_id(added_professor_id)

    assert added_professor_db_obj["name"] == fake_professor_info.name
    assert added_professor_db_obj["image"] == fake_professor_info.image
    assert added_professor_db_obj["phone"] == fake_professor_info.phone
    assert added_professor_db_obj["gender"] == fake_professor_info.gender


def test_get_professors(client, register_user):
    response, _, request_headers = register_user

    professor_client_mocker = ProfessorClientMocker(client, request_headers)

    _ = professor_client_mocker.post_fake_professors()
    get_professors_response = professor_client_mocker.get_all_professors()

    fetched_professors = get_professors_response.json()

    professor_model_fields = list(Professor.model_fields.keys())


    assert get_professors_response.status_code == 200

    for professor in fetched_professors:
        for professor_field in professor_model_fields:
            assert professor_field in professor, f"{professor_field} not in professor"

@pytest.mark.parametrize("feedback_type", ["upvotes", "downvotes"])
def test_feedback_professor(feedback_type, client, register_user):
    _, _, request_headers = register_user
  

    execute_generate_fake_profs_endpoint(client, FAKE_PROFESSORS_AMOUNT, request_headers)
    get_professors_response = execute_get_all_professor_endpoint(client, request_headers)
    fetched_professors = get_professors_response.json()
 
    professor_id = str(fetched_professors[0]["_id"])
    voted_professor_response = client.put(f"{ENDPOINTS.PROFESSORS}/{feedback_type}/{professor_id}", headers=request_headers)
    assert voted_professor_response.status_code == 201

    updated_professor_db_obj = client.get(f"{ENDPOINTS.PROFESSORS}/{professor_id}", headers=request_headers).json()
    professor_feedback_collection = updated_professor_db_obj[feedback_type]
    assert len(professor_feedback_collection) == 1, f"{feedback_type} were not added as expect"

    # Check that upvote object user id was the user id that feedbacked the professor
    current_user = client.get(f"{ENDPOINTS.USERS}", headers=request_headers).json()

    current_user_id = current_user["_id"]

    assert professor_feedback_collection[0]["user_id"] == current_user_id, "professor feedback object user id was not the user id that feedbacked the professor"



def test_comment_professor(client, register_user):
    response, _, request_headers = register_user

    response = execute_generate_fake_profs_endpoint(client, FAKE_PROFESSORS_AMOUNT, request_headers)
    get_professors_response = execute_get_all_professor_endpoint(client, request_headers)
    fetched_professors = get_professors_response.json()

    professor_id = str(fetched_professors[0]["_id"])
    comment_professor_response = execute_add_professor_comment_endpoint(client, request_headers, professor_id)
  

    assert comment_professor_response.status_code == 201

    updated_professor_db_obj = client.get(f"{ENDPOINTS.PROFESSORS}/{professor_id}", headers=request_headers).json()
    professor_comment_collection = updated_professor_db_obj["comments"]
    assert len(updated_professor_db_obj["comments"]) == 1, "Professor comment were not added correctly"
    current_user = client.get(f"{ENDPOINTS.USERS}", headers=request_headers).json()

    current_user_id = current_user["_id"]

    assert professor_comment_collection[0]["user_id"] == current_user_id, "professor feedback object user id was not the user id that feedbacked the professor"



'''
def test_delete_professor_comment(client, register_user):
    response, _, request_headers = register_user

    response = execute_generate_fake_profs_endpoint(client, FAKE_PROFESSORS_AMOUNT, request_headers)
    get_professors_response = execute_get_all_professor_endpoint(client, request_headers)
    fetched_professors = get_professors_response.json()

    professor_id = str(fetched_professors[0]["_id"])
    comment_professor_response = execute_add_professor_comment_endpoint(client, request_headers, professor_id)

    updated_professor_db_obj = client.get(f"{ENDPOINTS.PROFESSORS}/{professor_id}", headers=request_headers).json()
    professor_comment_collection = updated_professor_db_obj["comments"]
    current_professor_comments_amount = len(professor_comment_collection) 
 
    added_comment_id = professor_comment_collection[0]["_id"]

    delete_professor_comment_response = client.delete(
        f"{ENDPOINTS.PROFESSORS}/comments/{professor_id}/{added_comment_id}", headers=request_headers
    )

    updated_professor_db_obj = client.get(f"{ENDPOINTS.PROFESSORS}/{professor_id}", headers=request_headers).json()
    professor_comment_collection = updated_professor_db_obj["comments"]
    assert len(professor_comment_collection) == (current_professor_comments_amount-1), "Comment was not deleted correctly"
'''