from faker import Faker
from app.settings import APP_SETTINGS
import json
from ..utils.security import decode_jwt_token, verify_password


def test_register_user(client, register_user):

    """
    Test the user registration endpoint.

    This test ensures that when a new user is registered using the provided
    client and registration data, the response status code is 201, indicating 
    successful creation. It also checks that a token is returned in the 
    response JSON, confirming that the user has been authenticated.
    """
    response, mock_new_user_data, _ = register_user


    assert response.status_code == 201, f"Response status code expected to be 201, but got {response.status_code}"
    response_content = response.json()
    print('response_content["token"]', response_content["token"])
    assert response_content["token"] is not None, "Token not present auth endpoint response."

    token = response.json()["token"]
    jwt_payload = decode_jwt_token(token)
    user_id = jwt_payload["data"]["id"]

    users_db_mock = client.app.database[APP_SETTINGS.USERS_DB_NAME]
    new_user = users_db_mock.find_one(
        {"_id": user_id}    
    )
    

    assert verify_password(mock_new_user_data["password"], new_user["password"]), "Password not hashed correctly"
    assert new_user["email"] == mock_new_user_data["email"], "Email not stored correctly"
    assert new_user["name"] == mock_new_user_data["name"], "Name not stored correctly"

    # Try register user with the same email
    #assert register_response.status_code == 409
    #print('register_response', register_response)


   
def test_login_user(client, register_user):

    
    """
    Test the user login endpoint.

    This test ensures that when a user attempts to login with correct
    credentials, the response status code is 201, indicating successful
    authentication. It also checks that a token is returned in the response
    JSON, verifying that the user has been authenticated.
    """
    _, mock_new_user_data, _ = register_user

    # Try login with right password
    response = client.post(
        "/auth/login",
        json={"email": mock_new_user_data["email"], "password": mock_new_user_data["password"]},
    )
    assert response.status_code == 201
    assert "token" in response.json(), "Token not present auth endpoint response."

    # try login with wrong password
    response = client.post(
        "/auth/login",
        json={"email": mock_new_user_data["email"], "password": "coxinha123"},
    )

    response_text = json.loads(response.text)["detail"]
    assert response.status_code == 401
    assert response_text == "Password is not valid!"



def test_get_user_info(client, register_user):
    """
    Test the user info retrieval endpoint.

    This test ensures that when a user attempts to retrieve their information with a valid
    JWT token, the response status code is 200, indicating successful retrieval. It also
    checks that the response contains the expected user information.
    """
    response, mock_new_user_data, request_headers  = register_user
    
    response = client.get("/users/", headers=request_headers)
    fetch_user_info = response.json()
    assert response.status_code == 200, f"Response status code expected to be 200, but got {response.status_code}"
    assert mock_new_user_data["email"] in fetch_user_info["email"], "Email not present in user info response."
    
    