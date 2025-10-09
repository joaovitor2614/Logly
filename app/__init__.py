
from fastapi import FastAPI
from .database import db_lifespan
from .routers import register_routers
from .settings import APP_SETTINGS
from .middlewares import register_middlewares
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from pathlib import Path
import os

def create_app() -> FastAPI:

    app = FastAPI(
        title="Logly",
        version="1.0.0",
        lifespan=db_lifespan
    )
     
    register_middlewares(app)
    register_routers(app)
    if APP_SETTINGS.APP_MODE == "PROD":
        dist_dir = os.path.join(Path(os.path.dirname(__file__)).parent, "web", "dist")

        app.mount("/app", StaticFiles(directory=dist_dir, html=True), name="spa")
  



    return app


app = create_app()




