
from fastapi import FastAPI
from .database import register_db_connection
from .routers import register_routers
from .middlewares import register_middlewares
from fastapi.testclient import TestClient
import firebase_admin
from firebase_admin import credentials
from pathlib import Path
import os


def create_app(is_test_mode=False) -> FastAPI:

    app = FastAPI()
    register_db_connection(app)
    register_middlewares(app)
    register_routers(app)

    cred = credentials.Certificate(os.path.join(Path(__file__).parent.parent, "service-account.json"))
    firebase_admin.initialize_app(cred)
    


    return app if not is_test_mode else TestClient(app)


app = create_app()




