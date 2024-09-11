from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.values.tasks import Priority, Status


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