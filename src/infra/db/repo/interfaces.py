from abc import ABC, abstractmethod
from src.domain.entities.tasks import Task as TaskEntity


class TaskReader(ABC):

    @abstractmethod
    async def get_task_by_id(self, task_id: int):
        ...

    @abstractmethod
    async def get_all_tasks(self):
        ...





class TaskWriter(ABC):

    @abstractmethod
    async def delete_task(self, task: TaskEntity):
        ...

    @abstractmethod
    async def update_task(self, task: TaskEntity):
        ...

    @abstractmethod
    async def add_task(self, task: TaskEntity):
        ...


class UOW(ABC):

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...