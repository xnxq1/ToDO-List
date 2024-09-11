from dataclasses import dataclass, field
from uuid import UUID, uuid4

from src.domain.values.tasks import Title, Priority, Status


@dataclass(eq=False)
class Task:
    id: UUID = field(
        default_factory=uuid4,
        kw_only=True
    )
    title: Title
    priority: Priority
    status: Status

    def __eq__(self, other: 'Task'):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


