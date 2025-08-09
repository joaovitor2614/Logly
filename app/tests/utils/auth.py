
from app.core.token import JWTHandler
from fastapi import Response

def get_user_id_from_register_response(response: Response) -> str:
    jwt_handler = JWTHandler()
    token = response.json()["token"]
    jwt_payload = jwt_handler.decode_jwt_token(token)
    user_id = jwt_payload["data"]["id"]
    return user_id

def get_user_id_from_request_headers(request_headers: dict) -> str:
    token = request_headers["Authorization"].split(" ")[1]
    jwt_handler = JWTHandler()
    jwt_payload = jwt_handler.decode_jwt_token(token)
    user_id = jwt_payload["data"]["id"]
    return user_id