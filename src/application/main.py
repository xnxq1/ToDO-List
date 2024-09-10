from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title='ToDo List'
    )
    return app