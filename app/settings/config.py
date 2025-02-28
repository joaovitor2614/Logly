
from pydantic_settings import BaseSettings
from pydantic import Field



class Settings(BaseSettings):
    MONGO_DB_ATLAS_URI: str
    SECRET_KEY: str = "015a42020f023ac2c3eda3d45fe5ca3fef8921ce63589f6d4fcdef9814cd7fa7"
    JWT_ALGORITHM: str = "HS256"
    DB_NAME: str = "Users"
    