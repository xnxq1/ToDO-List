import pytest

from src.domain.entities.tasks import Task
from src.domain.values.tasks import Title, Priority, Status


def test_task():
    task = Task(100 ,Title('100'), Priority.low, Status.uncompleted)
    assert task.id == 100
    assert task.title.value == '100'
    assert task.priority == Priority.low
    assert task.status == Status.uncompleted
