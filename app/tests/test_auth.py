from faker import Faker
from app.settings import APP_SETTINGS
import json
from faker import Faker
from ..utils.security import verify_password
from app.tests.utils.wrapper.auth import AuthEndPointWrapper
from app.controllers.user import UserController
from app.tests.utils.auth import get_user_id_from_register_response

def test_register_user(client):

    """
    Test the user registration endpoint.

    This test ensures that when a new user is registered using the provided
    client and registration data, the response status code is 201, indicating 
    successful creation. It also checks that a token is returned in the 
    response JSON, confirming that the user has been authenticated.
    """
    fake = Faker()
    user_controller = UserController(client)
    auth_endpoint_mocker = AuthEndPointWrapper(client)
    mock_new_user_data = {"name": fake.name(), "email": fake.email(), "password": fake.password()}
    response = auth_endpoint_mocker.register(mock_new_user_data)


    assert response.status_code == 201, f"Response status code expected to be 201, but got {response.status_code}"
    response_content = response.json()

    assert response_content["token"] is not None, "Token not present auth endpoint response."


    user_id = get_user_id_from_register_response(response)

    new_user = user_controller.get_user_by_id(user_id)
    
    assert verify_password(mock_new_user_data["password"], new_user["password"]), "Password not hashed correctly"
    assert new_user["email"] == mock_new_user_data["email"], "Email not stored correctly"
    assert new_user["name"] == mock_new_user_data["name"], "Name not stored correctly"


   
def test_login_user(client, register_user):
    """
    Test the user login endpoint.

    This test ensures that when a user attempts to login with correct
    credentials, the response status code is 201, indicating successful
    authentication. It also checks that a token is returned in the response
    JSON, verifying that the user has been authenticated.
    """
    mock_new_user_data, _ = register_user
    auth_endpoint_mocker = AuthEndPointWrapper(client)
    # Try login with right password
    response = auth_endpoint_mocker.login(mock_new_user_data["email"], mock_new_user_data["password"])
    assert response.status_code == 201
    assert "token" in response.json(), "Token not present auth endpoint response."

    # try login with wrong password
    response = auth_endpoint_mocker.login(mock_new_user_data["email"], "coxinha123")

    response_text = json.loads(response.text)["detail"]
    assert response.status_code == 401
    assert response_text == "Password is not valid!"



