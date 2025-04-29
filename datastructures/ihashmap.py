from abc import abstractmethod
from typing import Iterator, Mapping, TypeVar


KT = TypeVar('KT')
VT = TypeVar('VT')


class IHashMap(Mapping[KT, VT]):
    """
    Interface for a HashMap.
    """

    @abstractmethod
    def __init__(self, initial_capacity=7, load_factor=0.75, data_type: type=object) -> None:
        """
        Initializes the HashMap with the given initial capacity and load factor.

        Args:
            initial_capacity (int): The initial capacity of the map.
            load_factor (float): The load factor for resizing the map.
            data_type (type): The type of values stored in the map.

        Returns:
            None
        """
        ...

    @abstractmethod
    def __getitem__(self, key: KT) -> VT:
        """
        Retrieves the value associated with the given key.

        Args:
            key (KT): The key to retrieve the value for.

        Returns:
            VT: The value associated with the key.
        """
        ...

    @abstractmethod
    def __setitem__(self, key: KT, value: VT) -> None:
        """
        Sets the value for the given key.

        Args:
            key (KT): The key to set the value for.
            value (VT): The value to set.

        Returns:
            None
        Raises:
            TypeError: If the value is not of the expected type.
            KeyError: If the key already exists in the map.
        """
        ...

    @abstractmethod
    def keys(self):
        """
        Returns an iterable of the `keys` in the map.

        Returns:
            Iterable[KT]: An iterable of the `keys` in the map.
        """
        ...
    
    @abstractmethod
    def values(self):
        """
        Returns an iterable of the `values` in the map.

        Returns:
            Iterable[VT]: An iterable of the `values` in the map.
        """
        ...
    
    @abstractmethod
    def items(self):
        """
        Returns an iterable of the `items` in the map.

        Returns:
            Iterable[tuple[KT, VT]]: An iterable of the `items` in the map.
        """
        ...

    @abstractmethod
    def __delitem__(self, key: KT) -> None:
        """
        Deletes the key-value pair associated with the given key.

        Args:
            key (KT): The key to delete.

        Returns:
            None
        Raises:
            KeyError: If the key does not exist in the map.
        """
        ...

    @abstractmethod
    def __contains__(self, key: KT) -> bool:
        """
        Checks if the map contains the specified key.

        Args:
            key (KT): The key to check for existence.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        ...

    @abstractmethod
    def __len__(self) -> int:
        """
        Returns the number of key-value pairs in the map.

        Returns:
            int: The number of key-value pairs in the map.
        """
        ...

    @abstractmethod
    def __iter__(self) -> Iterator[KT]:
        """
        Returns an iterator over the keys in the map.

        Returns:
            Iterator[KT]: An iterator over the keys in the map.
        """
        ...

    @abstractmethod
    def __str__(self) -> str:
        """
        Returns a string representation of the map.

        Returns:
            str: A string representation of the map.
        """
        ...

    @abstractmethod
    def __repr__(self) -> str:
        """
        Returns a string representation of the map for debugging.

        Returns:
            str: A string representation of the map for debugging.
        """
        ...

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """
        Checks if the map is equal to another object.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if the map is equal to the other object, False otherwise.
        """
        ...

    def __hash__(self) -> int:
        """
        This interface also acts as a base class with a hash method override that always raises a TypeError.
        HashMap objects are unhashable because they are mutable so this should always raise a TypeError.
        
        Raises:
            TypeError: Always raised to indicate that HashMap objects are unhashable.
        """
        raise TypeError("HashMap objects are unhashable")