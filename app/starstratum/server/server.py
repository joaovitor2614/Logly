
from fastapi import FastAPI
from dotenv import dotenv_values
from .database.connection import register_db_connection
from .middlewares.middlewares import register_middlewares




def create_app() -> FastAPI:

    app = FastAPI()
    register_db_connection(app)
    register_middlewares(app)

    return app


app = create_app()



