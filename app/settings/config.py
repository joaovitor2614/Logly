
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pydantic import Field

load_dotenv()

class Settings(BaseSettings):
    MONGO_DB_ATLAS_URI: str = "mongodb+srv://<username>:<password>@cluster0.q5szy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    SECRET_KEY: str = "015a42020f023ac2c3eda3d45fe5ca3fef8921ce63589f6d4fcdef9814cd7fa7"
    JWT_ALGORITHM: str = "HS256"
    USERS_DB_NAME: str = "Users"

    PROFESSORS_DB_NAME: str = "Professors"
    