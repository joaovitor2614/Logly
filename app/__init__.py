
from fastapi import FastAPI
from .database import db_lifespan
from .routers import register_routers
from .middlewares import register_middlewares


def create_app() -> FastAPI:

    app = FastAPI(
        title="Logly",
        version="1.0.0",
        lifespan=db_lifespan
    )
     
    register_middlewares(app)
    register_routers(app)


    return app


app = create_app()




