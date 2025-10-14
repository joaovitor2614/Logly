
from fastapi import FastAPI, Request

from .routers import register_routers
from .settings import APP_SETTINGS
from .middlewares import register_middlewares
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import traceback
import logging
import sys
from pathlib import Path
import os

def create_app() -> FastAPI:

    app = FastAPI(
        title="Logly",
        version="1.0.0",
 
    )

     
    register_middlewares(app)
    register_routers(app)

    logger = logging.getLogger("uvicorn.error")



    @app.exception_handler(Exception)
    async def exception_handler(request: Request, exc: Exception):

        print("🔥 ERROR on request:", request.url.path, file=sys.stderr)
        traceback.print_exc() 
 
        logger.exception("Unhandled exception in request")

        return JSONResponse(
            status_code=500,
            content={"detail": str(exc)},
        )
    if APP_SETTINGS.APP_MODE == "PROD":
        dist_dir = os.path.join(Path(os.path.dirname(__file__)).parent, "web", "dist")

        app.mount("/app", StaticFiles(directory=dist_dir, html=True), name="spa")
  



    return app


app = create_app()




