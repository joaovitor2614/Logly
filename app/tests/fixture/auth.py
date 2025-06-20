from faker import Faker
from app.tests.utils.wrapper.auth import AuthEndPointWrapper
from app.tests.utils.token import get_authorization_setted_request_headers_from_register_response
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
    auth_endpoint_mocker = AuthEndPointWrapper(client)
    mock_new_user_data = {"name": fake.name(), "email": fake.email(), "password": fake.password()}

    register_response = auth_endpoint_mocker.register(mock_new_user_data)

    request_headers = get_authorization_setted_request_headers_from_register_response(register_response)
   
    return mock_new_user_data, request_headers