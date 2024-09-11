from typing import List

from src.infra.db.converter import convert_db_model_to_task, convert_task_to_db_model
from src.infra.db.exceptions import NotTaskException
from src.infra.db.repo.base import SQLAlchemyBase, Filter
from src.infra.db.repo.interfaces import TaskReader, TaskWriter, UOW
from sqlalchemy import select
from src.infra.db.models import Task as TaskDb
from src.domain.entities.tasks import Task as TaskEntity



class TaskReaderImpl(SQLAlchemyBase, TaskReader):

    async def get_task_by_id(self, task_id: int) -> TaskEntity:
        task: TaskDb | None = await self.session.get(TaskDb, task_id)
        if task is None:
            raise NotTaskException(task_id)
        return convert_db_model_to_task(task)

    async def get_all_tasks(self, task_filter: Filter | None = None) -> List[TaskEntity]:
        if task_filter:
            query = select(TaskDb).filter_by(**task_filter)
        else:
            query = select(TaskDb)

        tasks = await self.session.execute(query)
        tasks = tasks.scalars().all()
        tasks = [convert_db_model_to_task(task) for task in tasks]
        return tasks


class TaskWriterImpl(SQLAlchemyBase, TaskWriter):


    async def delete_task(self, task: TaskEntity) -> None:
        task_db: TaskDb = convert_task_to_db_model(task)
        await self.session.delete(task_db)

    async def update_task(self, task: TaskEntity) -> None:
        task_db: TaskDb = convert_task_to_db_model(task)
        await self.session.merge(task_db)

    async def add_task(self, task: TaskEntity) -> None:
        task_db: TaskDb = convert_task_to_db_model(task)
        self.session.add(task_db)


class UnitOfWork(SQLAlchemyBase, UOW):

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()