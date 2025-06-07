from . import auth, users, well
from fastapi import FastAPI


class ENDPOINTS:
    USERS = "/users"
    AUTH = "/auth"
    WELL = "/well"

def register_routers(app: FastAPI):
    app.include_router(auth.router, tags=["auth"], prefix=ENDPOINTS.AUTH)
    app.include_router(users.router, tags=["users"], prefix=ENDPOINTS.USERS)
    app.include_router(well.router, tags=["well"], prefix=ENDPOINTS.WELL)



