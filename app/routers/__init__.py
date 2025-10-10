from . import auth, users, well
from fastapi import FastAPI


class ENDPOINTS:
    USERS = "/api/users"
    AUTH = "/api/auth"
    WELL = "/api/well"

routers_info = [
        {"router": auth.router, "prefix": ENDPOINTS.AUTH},
        {"router": users.router, "prefix": ENDPOINTS.USERS},
        {"router": well.router, "prefix": ENDPOINTS.WELL}
]

def register_routers(app: FastAPI):
    for route_info in routers_info:
        app.include_router(route_info["router"], prefix=route_info["prefix"])




