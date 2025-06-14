from app.tests.utils.auth import get_user_id_from_register_response
from ..controllers.user import UserController

def test_get_user_info(client, register_user):
    """
    Test the user info retrieval endpoint.

    This test ensures that when a user attempts to retrieve their information with a valid
    JWT token, the response status code is 200, indicating successful retrieval. It also
    checks that the response contains the expected user information.
    """
    mock_new_user_data, request_headers  = register_user
    
    response = client.get("/users/", headers=request_headers)
    fetch_user_info = response.json()
    assert response.status_code == 200, f"Response status code expected to be 200, but got {response.status_code}"
    assert mock_new_user_data["email"] in fetch_user_info["email"], "Email not present in user info response."
    
def test_generate_verify_account_code(client, register_user):
    mock_new_user_data, request_headers  = register_user
    
    response = client.post("/users/send-verification-code", headers=request_headers)
    assert response.status_code == 200


def test_verify_account_code(client, register_user):
    mock_new_user_data, request_headers  = register_user
    
    #response = client.post("/users/send-verification-code", headers=request_headers)

    #user_id = get_user_id_from_register_response(response)
    #assert response.status_code == 200
