from faker import Faker
import pytest
@pytest.fixture
def register_user(client):
    """
    Fixture to register a new user with mock data.

    Uses Faker to generate random user details and sends a POST request
    to the '/auth/register' endpoint. Returns the response and the mock 
    user data used for registration.

    Args:
        client: The test client to send requests.

    Returns:
        Tuple containing the response from the registration request and the mock user data.
    """

    fake = Faker()
    mock_new_user_data = {"name": fake.name(), "email": fake.email(), "password": fake.password()}
    print('mock_new_user_data', mock_new_user_data)
    response = client.post(
        "/auth/register",
        json=mock_new_user_data,
    )
    return response, mock_new_user_data