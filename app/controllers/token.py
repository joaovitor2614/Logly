from ..models.auth.auth import JWTPayload
from datetime import datetime, UTC, timedelta
from app.settings import APP_SETTINGS
import jwt


class JWTController:
    def __init__(self):
        pass
    def get_jwt_token_from_user_db_obj(self, user_db_obj: dict) -> str:
        jwt_payload = self.get_jwt_payload_from_user_db_obj(user_db_obj)
        self.set_jwt_payload_expires_time(jwt_payload)
        jwt_token = self.create_jwt_token_payload(jwt_payload)
        return jwt_token

    def get_jwt_payload_from_user_db_obj(self, user_db_obj: dict) -> JWTPayload:
        return JWTPayload(
            data={"email": user_db_obj["email"], "id": user_db_obj["_id"]}, 
            iat=datetime.now(UTC), 
            exp=datetime.now(UTC)
        )

    def create_jwt_token_payload(self, jwt_payload: JWTPayload) -> str:
        jwt_payload = jwt_payload.model_dump().copy()
        jwt_token = jwt.encode(jwt_payload, APP_SETTINGS.SECRET_KEY, algorithm=APP_SETTINGS.JWT_ALGORITHM)
        return jwt_token

    def set_jwt_payload_expires_time(self, jwt_payload: JWTPayload) -> JWTPayload:
        jwt_payload.exp += timedelta(minutes=APP_SETTINGS.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)