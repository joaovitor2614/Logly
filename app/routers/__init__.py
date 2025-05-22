from . import auth, users, upload
from fastapi import FastAPI


class ENDPOINTS:
    USERS = "/users"
    AUTH = "/auth"
    UPLOAD = "/upload"

def register_routers(app: FastAPI):
    app.include_router(auth.router, tags=["auth"], prefix=ENDPOINTS.AUTH)
    app.include_router(users.router, tags=["users"], prefix=ENDPOINTS.USERS)


