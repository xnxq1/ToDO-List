from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.api.responses import OkResponse
from src.application.di import AddTaskHandlerFactory, GetTasksHandlerFactory, UpdateTaskHandlerFactory, \
    DeleteTaskHandlerFactory
from src.domain.entities.tasks import Task
from src.domain.values.tasks import Priority, Title, Status
from src.infra.db.conn import dbmanager
from src.infra.db.repo.base import Filter
from src.infra.db.repo.repo import TaskReaderImpl, TaskWriterImpl, UnitOfWork
from src.logic.commands import AddTaskHandler, CreateTask, UpdateTaskHandler, UpdateTask, DeleteTaskHandler
from src.logic.queries import GetTasksHandler
from uuid import UUID
router = APIRouter(prefix='/tasks', tags=['Tasks'])


@router.post('/tasks')
async def add_task(
        task: CreateTask,
        handler: AddTaskHandler = Depends(AddTaskHandlerFactory)) -> OkResponse:

    await handler(task)
    return OkResponse()


@router.get('/tasks')
async def get_tasks(
        status: Status | None = None,
        priority: Priority | None = None,
        handler: GetTasksHandler = Depends(GetTasksHandlerFactory)) -> OkResponse:

    res = await handler(Filter(priority, status))
    return OkResponse(result=res)

@router.put('/tasks/{task_id}')
async def update_task(
        task_id: UUID,
        task: UpdateTask,
        handler: UpdateTaskHandler = Depends(UpdateTaskHandlerFactory)) -> OkResponse:

    await handler(task_id, task)
    return OkResponse()

@router.delete('/tasks/{task_id}')
async def delete_task(
        task_id: UUID,
        handler: DeleteTaskHandler = Depends(DeleteTaskHandlerFactory)) -> OkResponse:

    await handler(task_id)
    return OkResponse()



