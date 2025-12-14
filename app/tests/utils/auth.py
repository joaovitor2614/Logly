
from app.core.handler.token import jwt_handler
from fastapi import Response

def get_user_id_from_register_response(response: Response) -> str:

    token = response.json()["token"]
    jwt_payload = jwt_handler.decode_jwt_token(token)
    user_id = jwt_payload["data"]["id"]
    return user_id

def get_user_id_from_request_headers(request_headers: dict) -> str:
    token = request_headers["Authorization"].split(" ")[1]

    jwt_payload = jwt_handler.decode_jwt_token(token)
    user_id = jwt_payload["data"]["id"]
    return user_id