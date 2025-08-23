from fastapi import  status
from app.tests.utils.wrapper.user import UserEndPointWrapper
from ..controllers.user import UserController

def test_get_user_info(client, register_user):
    """
    Test the user info retrieval endpoint.

    This test ensures that when a user attempts to retrieve their information with a valid
    JWT token, the response status code is 200, indicating successful retrieval. It also
    checks that the response contains the expected user information.
    """
    mock_new_user_data, request_headers  = register_user
    user_endpoint_wrapper = UserEndPointWrapper(client, request_headers)
    response = user_endpoint_wrapper.get_users()
    fetch_user_info = response.json()
    assert response.status_code == 200, f"Response status code expected to be 200, but got {response.status_code}"
    assert mock_new_user_data["email"] in fetch_user_info["email"], "Email not present in user info response."

'''
def test_delete_user(mocker, client, register_user):
    mock_new_user_data, request_headers  = register_user
    user_controller = UserController(client)
    user_endpoint_wrapper = UserEndPointWrapper(client, request_headers)
    response = user_endpoint_wrapper.delete_user()
    http_exception_mocker = mocker.patch("fastapi.HTTPException")
    user_db_obj = user_controller.get_user_by_email(mock_new_user_data["email"])
    http_exception_mocker.assert_called_once_with(status_code=status.HTTP_404_NOT_FOUND)
    assert response.status_code == 200
'''


def test_delete_user_account(client, register_user):
    mock_new_user_data, request_headers  = register_user
    user_id = mock_new_user_data["_id"]
    user_controller = UserController(client)
    user_endpoint_wrapper = UserEndPointWrapper(client, request_headers)
    response = user_endpoint_wrapper.delete_user()
    assert response.status_code == 200