from collections.abc import Callable
from dataclasses import dataclass
from functools import wraps

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.values.tasks import Priority, Status
from src.infra.db.exceptions import RepoException


class SQLAlchemyBase:

    def __init__(self, session: AsyncSession):
        self.session = session

@dataclass
class Filter:
    priority: Priority | None = None
    status: Status | None = None

    def __iter__(self):
        return iter({
            'priority': self.priority,
            'status': self.status}.items())



def check_exception(func: Callable):
    @wraps(func)
    async def inner(*args, **kwargs):
        try:
            res = await func(*args, **kwargs)
            return res
        except SQLAlchemyError as err:
            raise RepoException()

    return inner