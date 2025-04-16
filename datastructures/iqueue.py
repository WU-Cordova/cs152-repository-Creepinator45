from abc import abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class IQueue(Generic[T]):
    ''' Interface for a queue data structure '''

    @abstractmethod
    def enqueue(self, item: T) -> None:
        ...

    @abstractmethod
    def dequeue(self) -> T:
        ...

    @abstractmethod
    def front(self) -> T:
        ...

    @abstractmethod
    def back(self) -> T:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...

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
    def __str__(self) -> str:
        ...

    @abstractmethod
    def __repr__(self) -> str:
        ...
