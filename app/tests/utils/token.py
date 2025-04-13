from fastapi import Response

def get_authorization_setted_request_headers_from_register_response(response: Response):
    """
    Creates a dictionary with the 'Authorization' key and a Bearer token
    value to be used in the headers of a request, given a response from a
    register endpoint.

    Args:
        response (Response): The response from a register endpoint.

    Returns:
        A dictionary with the 'Authorization' key and a Bearer token value.
    """

    token = response.json()["token"]
    request_headers = get_bearer_token_setted_request_headers(token)
    return request_headers

def get_bearer_token_setted_request_headers(token: str):
    
    """
    Creates a dictionary with the 'Authorization' key and a Bearer token
    value to be used in the headers of a request.

    Args:
        token (str): The bearer token to be used.

    Returns:
        A dictionary with the 'Authorization' key and a Bearer token value.
    """
    return {"Authorization": f"Bearer {token}"}