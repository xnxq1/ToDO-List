from dataclasses import dataclass

from src.infra.db.repo.interfaces import TaskReader


@dataclass
class GetTasksHandler:
    task_reader: TaskReader

    async def __call__(self):
        tasks = await self.task_reader.get_all_tasks()
        return tasks