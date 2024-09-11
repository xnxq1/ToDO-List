from src.domain.values.tasks import Title
from src.infra.db.models import Task as TaskDb
from src.domain.entities.tasks import Task as TaskEntity



def convert_db_model_to_task(task: TaskDb) -> TaskEntity:
    return TaskEntity(
        id=task.id,
        title=Title(task.title),
        priority=task.priority,
        status=task.status
        )


def convert_task_to_db_model(task: TaskEntity) -> TaskDb:
    return TaskDb(
        id=task.id,
        title=task.title.to_row(),
        priority=task.priority,
        status=task.status
        )
