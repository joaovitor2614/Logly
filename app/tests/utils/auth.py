from fastapi import Response
from fastapi.testclient import TestClient

def execute_register_endpoint(
    client: TestClient,
    user_data: dict
) -> Response:
    """
    Sends a POST request to the '/auth/register' endpoint with the given user_data.
    
    Args:
        client (TestClient): The FastAPI test client to send the request.
        user_data (dict): The user data to be sent in the request.

    Returns:
        Response: The response from the endpoint.
    """
    response = client.post(
        "/auth/register",
        json=user_data,
    )
    return response