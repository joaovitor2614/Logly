from faker import Faker
from app.settings import APP_SETTINGS
from ..utils.security import decode_jwt_token, verify_password
from app.tests.utils.auth import execute_register_endpoint

def test_register_user(client):

    """
    Test the user registration endpoint.

    This test ensures that when a new user is registered using the provided
    client and registration data, the response status code is 201, indicating 
    successful creation. It also checks that a token is returned in the 
    response JSON, confirming that the user has been authenticated.
    """
    fake = Faker()
    mock_new_user_data = {"name": fake.name(), "email": fake.email(), "password": fake.password()}
    response = execute_register_endpoint(client, mock_new_user_data)

    assert response.status_code == 201, f"Response status code expected to be 201, but got {response.status_code}"
    assert "token" in response.json(), "Token not present auth endpoint response."

    token = response.json()["token"]
    jwt_payload = decode_jwt_token(token)
    user_id = jwt_payload["data"]["id"]

    users_db_mock = client.app.database[APP_SETTINGS.USERS_DB_NAME]
    new_user = users_db_mock.find_one(
        {"_id": user_id}    
    )
    

    assert verify_password(mock_new_user_data["password"], new_user["password"]), "Password not hashed correctly"
    assert new_user["email"] == mock_new_user_data["email"], "Email not stored correctly"
    #assert new_user["name"] == mock_new_user_data["name"], "Name not stored correctly"


def test_login_user(client, register_user):

    
    """
    Test the user login endpoint.

    This test ensures that when a user attempts to login with correct
    credentials, the response status code is 201, indicating successful
    authentication. It also checks that a token is returned in the response
    JSON, verifying that the user has been authenticated.
    """
    _, mock_new_user_data = register_user
    response = client.post(
        "/auth/login",
        json={"email": mock_new_user_data["email"], "password": mock_new_user_data["password"]},
    )
    assert response.status_code == 201
    assert "token" in response.json(), "Token not present auth endpoint response."
    