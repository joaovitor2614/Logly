
from app.core.token import JWTHandler
from fastapi import Response

def get_user_id_from_register_response(response: Response) -> str:
    jwt_handler = JWTHandler()
    token = response.json()["token"]
    jwt_payload = jwt_handler.decode_jwt_token(token)
    user_id = jwt_payload["data"]["id"]
    return user_id