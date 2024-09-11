from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import ORJSONResponse
from functools import partial
from typing import Callable, Awaitable

from starlette import status

from src.application.api.responses import ErrorResponse
from src.domain.values.base import BaseCustomException, BaseCustomException
from src.domain.values.tasks import TooLongTitleException



def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(BaseCustomException, error_handler(500))
    app.add_exception_handler(TooLongTitleException, error_handler(status.HTTP_400_BAD_REQUEST))
    app.add_exception_handler(Exception, unknown_exception_handler)


def app_error_handler(request: Request, exc: BaseCustomException, status_code: int) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=status_code,
        content=ErrorResponse(status=status_code, error=exc.message)
    )

def error_handler(status_code: int) -> Callable[..., Awaitable[ORJSONResponse]]:
    return partial(app_error_handler, status_code=status_code)

def unknown_exception_handler(request: Request, exc: Exception) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=500,
        content=ErrorResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR, error='Unknown')
    )

