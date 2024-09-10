from dataclasses import dataclass, field
from uuid import uuid4


from src.domain.values.tasks import Title, Priority, Status


@dataclass(eq=False)
class Task:
    id: int
    title: Title
    priority: Priority
    status: Status

    def __eq__(self, other: 'Task'):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


    def change_priority(self, priority: Priority):
        self.priority = priority

    def change_status(self, status: Status):
        self.status = status

