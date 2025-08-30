
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from pydantic import Field

load_dotenv()

class Settings(BaseSettings):
    MONGO_DB_ATLAS_URI: str = "mongodb+srv://<username>:<password>@cluster0.q5szy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    SECRET_KEY: str = "015a42020f023ac2c3eda3d45fe5ca3fef8921ce63589f6d4fcdef9814cd7fa7"
    JWT_ALGORITHM: str = "HS256"
    USERS_DB_NAME: str = "Users"
    WELLS_DB_NAME: str = "Wells"
    WELLS_DATA_DB_NAME: str = "WellsData"
    VERIFY_ACCOUNT_SENDER_EMAIL_ADDRESS: str = "WxG9i@example.com"
    VERIFY_ACCOUNT_SENDER_EMAIL_PASSWORD: str = "12345654"
    DB_NAME: str = "MyDB"
    APP_BASE_URL: str = "http://localhost:5173"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60   # 12 hours


