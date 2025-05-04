
from fastapi import FastAPI
from .database import db_lifespan
from .routers import register_routers
from .middlewares import register_middlewares

from pathlib import Path

import os


def create_app() -> FastAPI:

    app = FastAPI(
        title="Mamata ou Cilada",
        version="1.0.0",
        lifespan=db_lifespan
    )
     
    register_middlewares(app)
    register_routers(app)


    return app


app = create_app()




