from dataclasses import dataclass

from uuid import UUID
from src.domain.values.tasks import Priority, Status, Title
from src.infra.db.repo.interfaces import TaskWriter, UOW, TaskReader
from src.domain.entities.tasks import Task

@dataclass
class CreateTask:
    title: str
    priority: Priority
    status: Status

@dataclass
class UpdateTask:
    title: str
    priority: Priority
    status: Status

@dataclass
class AddTaskHandler:
    task_writer: TaskWriter
    uow: UOW

    async def __call__(self, task: CreateTask):
        task.title = Title(task.title)
        task = Task(title=task.title, priority=task.priority, status=task.status)
        await self.task_writer.add_task(task)
        await self.uow.commit()


@dataclass
class UpdateTaskHandler:
    task_writer: TaskWriter
    uow: UOW

    async def __call__(self, task_id, task: UpdateTask) -> None:
        task.title = Title(task.title)
        task = Task(id=task_id, title=task.title, priority=task.priority, status=task.status)
        await self.task_writer.update_task(task)
        await self.uow.commit()


@dataclass
class DeleteTaskHandler:
    task_reader: TaskReader
    task_writer: TaskWriter
    uow: UOW

    async def __call__(self, task_id: UUID) -> None:
        await self.task_reader.get_task_by_id(task_id)
        await self.task_writer.delete_task(task_id)
        await self.uow.commit()

