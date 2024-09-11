from dataclasses import dataclass

from src.infra.db.repo.base import Filter
from src.infra.db.repo.interfaces import TaskReader


@dataclass
class GetTasksHandler:
    task_reader: TaskReader

    async def __call__(self, task_filter: Filter | None = None):
        if task_filter is not None:
            task_filter = {key: value for key, value in task_filter if value is not None}
        tasks = await self.task_reader.get_all_tasks(task_filter)
        return tasks