from dataclasses import dataclass
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession, async_sessionmaker

from src.infra.config import settings

class DBManager:

    def __init__(self):
        self.engine = create_async_engine(
        url=settings.DATABASE_URL,
        echo=True)
        self.session_factory = async_sessionmaker(bind=self.engine, autoflush=False, expire_on_commit=False)

    async def build_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


dbmanager = DBManager()



