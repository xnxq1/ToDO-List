import enum
from dataclasses import dataclass

from src.domain.values.base import BaseValueObject, BaseDomainException, VT


@dataclass
class TooLongTitleException(BaseDomainException):
    title: str

    @property
    def message(self):
        return f'Слишком большой текст: {self.title[:255]}'


@dataclass
class Title(BaseValueObject[str]):

    def validate(self):
        if len(self.value) > 255:
            raise TooLongTitleException(self.value)

    def to_row(self) -> str:
        return str(self.value)


class Priority(enum.Enum):
    high = 'high'
    medium = 'medium'
    low = 'low'

class Status(enum.Enum):
    completed = 'completed'
    uncompleted = 'uncompleted'
