from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.__bag: dict[T, int] = {}

        if items is not None:
            for item in items:
                self.add(item)
    
    def add(self, item: T) -> None:
        if item is None:
            raise TypeError
        
        if item in self.__bag:
            self.__bag[item] += 1
        else:
            self.__bag[item] = 1

    def remove(self, item: T) -> None:
        if item not in self.__bag:
            raise ValueError
        
        self.__bag[item] -= 1
        if self.__bag[item] == 0:
            del self.__bag[item]

    def count(self, item: T) -> int:
        if item not in self.__bag:
            return 0
        return self.__bag[item]

    def __len__(self) -> int:
        total = 0
        for itemCount in self.__bag.values():
            total += itemCount
        return total

    def distinct_items(self) -> Iterable[T]:
        return self.__bag.keys()

    def __contains__(self, item) -> bool:
        return item in self.__bag

    def clear(self) -> None:
        self.__bag.clear()