from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.api.responses import OkResponse
from src.domain.entities.tasks import Task
from src.domain.values.tasks import Priority, Title, Status
from src.infra.db.conn import dbmanager
from src.infra.db.repo.repo import TaskReaderImpl, TaskWriterImpl, UnitOfWork
from src.logic.commands import AddTaskHandler, CreateTask, UpdateTaskHandler, UpdateTask, DeleteTaskHandler
from src.logic.queries import GetTasksHandler
from uuid import UUID
router = APIRouter(prefix='/tasks', tags=['Tasks'])


@router.post('/tasks')
async def add_task(task: CreateTask, session: AsyncSession = Depends(dbmanager.build_session)) -> OkResponse:
    repo = TaskWriterImpl(session=session)
    uow = UnitOfWork(session=session)
    await AddTaskHandler(repo, uow)(task)

    return OkResponse()


@router.get('/tasks')
async def get_tasks(session: AsyncSession = Depends(dbmanager.build_session)) -> OkResponse:
    repo = TaskReaderImpl(session=session)
    res = await GetTasksHandler(repo, )()

    return OkResponse(result=res)

@router.put('/tasks/{task_id}')
async def update_task(task_id: UUID, task: UpdateTask, session: AsyncSession = Depends(dbmanager.build_session)) -> OkResponse:
    repo = TaskWriterImpl(session=session)
    uow = UnitOfWork(session=session)
    await UpdateTaskHandler(repo, uow)(task_id, task)

    return OkResponse()

@router.delete('/tasks/{task_id}')
async def delete_task(task_id: UUID, session: AsyncSession = Depends(dbmanager.build_session)) -> OkResponse:
    repor = TaskReaderImpl(session=session)
    repow = TaskWriterImpl(session=session)
    uow = UnitOfWork(session=session)
    await DeleteTaskHandler(repor, repow, uow)(task_id)

    return OkResponse()



