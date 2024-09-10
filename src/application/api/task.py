from fastapi import APIRouter

from src.domain.entities.tasks import Task
from src.domain.values.tasks import Priority, Title

router = APIRouter(prefix='/tasks', tags=['Tasks'])


@router.post('')
async def index():
    ...