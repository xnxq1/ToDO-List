from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from dataclasses import dataclass

VT = TypeVar('VT')


@dataclass()
class BaseValueObject(ABC, Generic[VT]):
    value: VT


    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self):
        ...

    @abstractmethod
    def to_row(self) -> VT:
        ...



class BaseCustomException(Exception):
    @property
    def message(self):
        return f'Произошла ошибка'