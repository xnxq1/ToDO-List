from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.db.conn import dbmanager
from src.infra.db.repo.repo import UnitOfWork, TaskWriterImpl, TaskReaderImpl
from src.logic.commands import AddTaskHandler, UpdateTaskHandler, DeleteTaskHandler
from src.logic.queries import GetTasksHandler


async def AddTaskHandlerFactory(session: AsyncSession = Depends(dbmanager.build_session)) -> AddTaskHandler:
    repo = TaskWriterImpl(session=session)
    uow = UnitOfWork(session=session)
    return AddTaskHandler(repo, uow)


async def GetTasksHandlerFactory(session: AsyncSession = Depends(dbmanager.build_session)) -> GetTasksHandler:
    repo = TaskReaderImpl(session=session)
    return GetTasksHandler(repo)


async def UpdateTaskHandlerFactory(session: AsyncSession = Depends(dbmanager.build_session)) -> UpdateTaskHandler:
    repo = TaskWriterImpl(session=session)
    uow = UnitOfWork(session=session)
    return UpdateTaskHandler(repo, uow)


async def DeleteTaskHandlerFactory(session: AsyncSession = Depends(dbmanager.build_session)) -> DeleteTaskHandler:
    repor = TaskReaderImpl(session=session)
    repow = TaskWriterImpl(session=session)
    uow = UnitOfWork(session=session)
    return DeleteTaskHandler(repor, repow, uow)