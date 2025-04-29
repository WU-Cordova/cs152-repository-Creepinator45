from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class IStack(Generic[T], ABC):

    @abstractmethod
    def push(self, item: T) -> None:
        ...

    @abstractmethod
    def pop(self) -> T:
        ...

    @abstractmethod
    def peek(self) -> T:
        ...

    @property
    @abstractmethod
    def empty(self) -> bool:
        ...

    @abstractmethod
    def clear(self) -> None:
        ...
    
    @abstractmethod
    def __contains__(self, item: T) -> bool:
        ...
    
    @abstractmethod
    def __eq__(self, other: object) -> bool:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...

    @abstractmethod
    def __str__(self) -> str:
        ...

    @abstractmethod
    def __repr__(self) -> str:
        ...