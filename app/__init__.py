
from fastapi import FastAPI
from .routers import auth, users, professors
from .database.connection import register_db_connection
from .middlewares.middlewares import register_middlewares




def create_app() -> FastAPI:

    app = FastAPI()
    register_db_connection(app)
    register_middlewares(app)
    app.include_router(auth.router, tags=["auth"], prefix="/auth")
    app.include_router(users.router, tags=["users"], prefix="/users")
    app.include_router(professors.router, tags=["professors"], prefix="/professors")


    return app


app = create_app()




