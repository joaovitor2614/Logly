from ...models.auth.auth import JWTPayload
from datetime import datetime, UTC, timedelta
from app.settings import APP_SETTINGS
import jwt


class JWTHandler:
    
    def get_jwt_token_from_user_db_obj(self, user_db_obj: dict, custom_exp_time_minutes: int | None = None) -> str:
        jwt_payload = self.get_jwt_payload_from_user_db_obj(user_db_obj)
        self.set_jwt_payload_expires_time(jwt_payload, custom_exp_time_minutes)
        jwt_token = self.create_jwt_token_payload(jwt_payload)
        return jwt_token

    def get_jwt_payload_from_user_db_obj(self, user_db_obj: dict) -> JWTPayload:
        return JWTPayload(
            data={"email": user_db_obj["email"], "id": user_db_obj["_id"]}, 
            iat=datetime.now(UTC), 
            exp=datetime.now(UTC)
        )

    def decode_jwt_token(self, token: str):
        payload = jwt.decode(token, APP_SETTINGS.SECRET_KEY, algorithms=[APP_SETTINGS.JWT_ALGORITHM])
        return payload


    def create_jwt_token_payload(self, jwt_payload: JWTPayload) -> str:
        jwt_payload = jwt_payload.model_dump().copy()
        jwt_token = jwt.encode(jwt_payload, APP_SETTINGS.SECRET_KEY, algorithm=APP_SETTINGS.JWT_ALGORITHM)
        return jwt_token

    def set_jwt_payload_expires_time(self, jwt_payload: JWTPayload, custom_exp_time_minutes: int | None = None):
        exp_time_minutes = APP_SETTINGS.JWT_ACCESS_TOKEN_EXPIRE_MINUTES if custom_exp_time_minutes is None else custom_exp_time_minutes
        jwt_payload.exp += timedelta(minutes=exp_time_minutes)

jwt_handler = JWTHandler()