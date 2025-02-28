from fastapi import FastAPI
from pymongo import MongoClient, server_api
from dotenv import load_dotenv
import os

config = load_dotenv()

DB_NAME = os.getenv("DB_NAME")
MONGO_DB_ATLAS_URI = os.getenv("MONGO_DB_ATLAS_URI")

def register_db_connection(app: FastAPI):
    @app.on_event("startup")
    def startup_db_client():
        app.mongodb_client = MongoClient(MONGO_DB_ATLAS_URI, server_api=server_api.ServerApi(version="1", strict=True, deprecation_errors=True))
        app.database = app.mongodb_client[DB_NAME]
        app.mongodb_client.admin.command("ping")

        print("Connected to the MongoDB database!")

    @app.on_event("shutdown")
    def shutdown_db_client():
        app.mongodb_client.close()