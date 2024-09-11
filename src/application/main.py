from fastapi import FastAPI

from src.application.api.exceptions import setup_exception_handlers
from src.application.api.router import router as router_task

def create_app() -> FastAPI:
    app = FastAPI(
        title='ToDo List'
    )
    app.include_router(router_task)
    setup_exception_handlers(app)
    return app