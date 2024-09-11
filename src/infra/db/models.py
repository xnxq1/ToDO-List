from sqlalchemy import CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.domain.values.tasks import Priority, Status
from uuid import UUID, uuid4


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = 'Task'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    title: Mapped[str] = mapped_column(nullable=False)
    priority: Mapped[Priority] = mapped_column(nullable=False)
    status: Mapped[Status] = mapped_column(nullable=False)

    __table_args__ = (
        CheckConstraint('length(title) <= 255', name='check_title_length'),
    )