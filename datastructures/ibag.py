from abc import ABC, abstractmethod
from typing import Optional, TypeVar, Generic, Iterable

T = TypeVar('T')  # Generic type for items in the Bag

class IBag(ABC, Generic[T]):
    """
    Interface for a Bag (MultiSet) data structure.
    """

    @abstractmethod
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        """
        Initializes the Bag.
        """
        pass
    
    @abstractmethod
    def add(self, item: T) -> None:
        """
        Adds an item to the Bag.
        
        Args:
            item (T): The item to add.

        Returns:
            None

        Raises:
            TypeError: If the item is None.

        Examples:
            >>> bag: Bag[int] = Bag()
            >>> bag.add(1)
            >>> bag.add(2)
            >>> bag.add(1)

            >>> bag.count(1)
            2
            >>> bag.count(2)
            1
            >>> bag.add(None)
            TypeError: Item cannot be None
        """
        pass

    @abstractmethod
    def remove(self, item: T) -> None:
        """
        Removes one occurrence of the item from the Bag.
        
        Args:
            item (T): The item to remove.

        Returns:
            None

        Raises:
            ValueError: If the item is not present in the Bag.

        Examples:
            >>> bag: Bag[int] = Bag()
            >>> bag.add(1)
            >>> bag.add(2)
            >>> bag.add(1)

            >>> bag.remove(1)
            >>> bag.count(1)
            1
            >>> bag.remove(1)
            >>> bag.count(1)
            0
            >>> bag.remove(1)
            ValueError: Item not found in Bag
        """
        pass
    
    @abstractmethod
    def count(self, item: T) -> int:
        """
        Returns the number of occurrences of the item in the Bag.
        
        Args:
            item (T): The item to count.

        Returns:
            int: The number of occurrences of the item.

        Examples:
            >>> bag: Bag[int] = Bag()
            >>> bag.add(1)
            >>> bag.add(2)
            >>> bag.add(1)

            >>> bag.count(1)
            2
            >>> bag.count(2)
            1
            >>> bag.count(3)
            0
        """
        pass
    
    @abstractmethod
    def __len__(self) -> int:
        """
        Returns the total number of items in the Bag (including duplicates).
        
        Returns:
            int: The total number of items in the Bag.

        Examples:
            >>> bag: Bag[int] = Bag()
            >>> bag.add(1)
            >>> bag.add(2)
            >>> bag.add(1)

            >>> bag.size()
            3
        """
        pass
    
    @abstractmethod
    def distinct_items(self) -> Iterable[T]:
        """
        Returns an iterable of the distinct items in the Bag.
        
        Returns:
            Iterable[T]: An iterable of the distinct items in the Bag.
        """
        pass
    
    @abstractmethod
    def __contains__(self, item: T) -> bool:
        """
        Checks if the Bag contains the specified item.
        
        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item is present in the Bag, False otherwise.

        Examples:
            >>> bag: Bag[int] = Bag()
            >>> bag.add(1)
            >>> bag.add(2)
            >>> bag.add(1)

            >>> bag.contains(1)
            True
            >>> bag.contains(2)
            True
            >>> bag.contains(3)
            False
        """
        pass
    
    @abstractmethod
    def clear(self) -> None:
        """
        Removes all items from the Bag.
        """
        pass