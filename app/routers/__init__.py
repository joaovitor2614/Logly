from . import auth, users, professors
from fastapi import FastAPI

def register_routers(app: FastAPI):
    app.include_router(auth.router, tags=["auth"], prefix="/auth")
    app.include_router(users.router, tags=["users"], prefix="/users")
    app.include_router(professors.router, tags=["professors"], prefix="/professors")

