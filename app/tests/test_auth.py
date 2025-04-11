from faker import Faker





def test_register_user(client, register_user):

    """
    Test the user registration endpoint.

    This test ensures that when a new user is registered using the provided
    client and registration data, the response status code is 201, indicating 
    successful creation. It also checks that a token is returned in the 
    response JSON, confirming that the user has been authenticated.
    """

    response, _ = register_user
    assert response.status_code == 201
    assert "token" in response.json(), "Token not present auth endpoint response."


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
    