from app.utils.security import decode_jwt_token, verify_password
from fastapi import Response

def get_user_id_from_register_response(response: Response) -> str:
    token = response.json()["token"]
    jwt_payload = decode_jwt_token(token)
    user_id = jwt_payload["data"]["id"]
    return user_id