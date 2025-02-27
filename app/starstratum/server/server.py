
from fastapi import FastAPI
from .routers import auth
from .database.connection import register_db_connection
from .middlewares.middlewares import register_middlewares




def create_app() -> FastAPI:

    app = FastAPI()
    register_db_connection(app)
    register_middlewares(app)
    app.include_router(auth.router, tags=["auth"], prefix="/auth")

    return app


app = create_app()



