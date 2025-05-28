from fastapi import FastAPI
from pymongo import MongoClient, server_api
from app.settings import APP_SETTINGS
from contextlib import asynccontextmanager
import os

@asynccontextmanager
def db_lifespan(app: FastAPI):
    app.mongodb_client = MongoClient(APP_SETTINGS.MONGO_DB_ATLAS_URI, server_api=server_api.ServerApi(version="1", strict=True, deprecation_errors=True))
    app.database = app.mongodb_client[APP_SETTINGS.DB_NAME]
    app.mongodb_client.admin.command("ping")
    yield
    app.mongodb_client.close()

