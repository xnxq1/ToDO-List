from fastapi import FastAPI
from src.application.api.task import router as router_task

def create_app() -> FastAPI:
    app = FastAPI(
        title='ToDo List'
    )
    app.include_router(router_task)
    return app