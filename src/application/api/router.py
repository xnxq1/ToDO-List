from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.api.responses import OkResponse
from src.domain.entities.tasks import Task
from src.domain.values.tasks import Priority, Title
from src.infra.db.conn import dbmanager
from src.infra.db.repo.repo import TaskReaderImpl

router = APIRouter(prefix='/tasks', tags=['Tasks'])


@router.get('')
async def index(session: AsyncSession = Depends(dbmanager.build_session)) -> OkResponse:
    repo = TaskReaderImpl(session=session)
    r = await repo.get_all_tasks()
    print(r)
    return OkResponse()
