from . import auth, users
from fastapi import FastAPI


class ENDPOINTS:
    USERS = "/users"
    AUTH = "/auth"

def register_routers(app: FastAPI):
    app.include_router(auth.router, tags=["auth"], prefix=ENDPOINTS.AUTH)
    app.include_router(users.router, tags=["users"], prefix=ENDPOINTS.USERS)



