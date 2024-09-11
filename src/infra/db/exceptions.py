from dataclasses import dataclass

from src.domain.values.base import BaseCustomException


@dataclass
class NotTaskException(BaseCustomException):
    task_id: int

    @property
    def message(self):
        return f'Задачи с id {self.task_id} не существует'

class RepoException(BaseCustomException):
    @property
    def message(self):
        return f'Ошибка репозитория'