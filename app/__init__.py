
from fastapi import FastAPI
from .database import register_db_connection
from .routers import register_routers
from .middlewares import register_middlewares

import firebase_admin
from pathlib import Path

import os


def create_app() -> FastAPI:

    app = FastAPI()

    register_db_connection(app)
     
    register_middlewares(app)
    register_routers(app)


    return app


app = create_app()




