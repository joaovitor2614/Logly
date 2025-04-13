from . import auth, users, professors, upload
from fastapi import FastAPI


class ENDPOINTS:
    PROFESSORS = "/professors"
    USERS = "/users"
    AUTH = "/auth"
    UPLOAD = "/upload"

def register_routers(app: FastAPI):
    app.include_router(auth.router, tags=["auth"], prefix=ENDPOINTS.AUTH)
    app.include_router(users.router, tags=["users"], prefix=ENDPOINTS.USERS)
    app.include_router(professors.router, tags=["professors"], prefix=ENDPOINTS.PROFESSORS)
    app.include_router(upload.router, tags=["upload"], prefix=ENDPOINTS.UPLOAD)

