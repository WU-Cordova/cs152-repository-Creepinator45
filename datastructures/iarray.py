# datastructures.iarray.IArray

""" This module defines an Array interface that represents a one-dimensional array. 
    This file lists the stipulations and more information on the methods and their expected behavior.
    YOU SHOULD NOT MODIFY THIS FILE.
    Implement the Array class in the array.py file.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Iterator, Sequence
import os
from typing import Any, Generic, TypeVar, overload

T = TypeVar('T', bound=Any)


class IArray(Sequence[T], Generic[T], ABC):
    """Array representing a one-dimensional array that grows dynamically. Supports the bracket operator for getting and 
        setting items in the array, the length operator, the equality and non-equality operators, the iterator and reversed iterator operators,
        the delete operator, the contains operator, the clear method, the string representation, and the resize method.
    """   

    @abstractmethod
    def __init__(self, starting_sequence: Sequence[T], data_type: type=object) -> None:
        """ Array Constructor. Initializes the Array with a default capacity (default: 0) and default value (default: None).
            The Array should manage a physical size (the size of the internal numpy array) and a logical size (the number of items in the Array).

        Examples:
            >>> array = Array[int](starting_sequence=[], data_type=int)
            >>> print(repr(array))
            Array(logical size: 0, items: [], physical size: 0, data type: <class 'int'>)
            >>> array = Array[int](starting_sequence=[1, 2, 3, 4, 5], data_type=int)
            >>> print(repr(array))
            Array(logical size: 5, items: [1, 2, 3, 4, 5], physical size: 5, data type: <class 'int'>)
            >>> array = Array[int]([num for num in range(15)], data_type=int)
            >>> print(repr(array))
            Array(logical size: 15, items: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], physical size: 15, data type: <class 'int'>)
        
        Args:
            sequence (Sequence[T]): the desired sequence type to initialize the Array with.
            data_type (type): the desired data type to initialize the Array with (default=object).

        Returns:
            None
        
        Raises:
            ValueError: if sequence is not a valid sequence type.
            ValueError: if data_type is not a valid data type.
        """
        pass

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    @abstractmethod
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        """ Bracket operator for getting an item (via int) or items (via slice) in an Array. If index is an integer,
            return the item at the index. If index is a slice, return the items at the slice. Supports wrap-around
            indexing via negative indixes.

        Examples:
            >>> array = Array[str](starting_sequence=['zero', 'one' , 'two', 'three', 'four'], data_type=str)
            >>> print(repr(str(array[1]))) # invokes __getitem__ with an `int` for the index.
            'one'
            >>> print(array[1:3]) # invokes __getitem__ with a `slice` for the index.
            ['one', 'two']
            >>> array = Array[str](starting_sequence=['zero', 'one', 'two', 'three', 'four'], data_type=str)
            >>> print(repr(str(array[-1]))) # invokes __getitem__ with a negative `int` for the index.
            'four'
            >>> print(array[-3:]) # invokes __getitem__ with a `slice` for the index.
            ['two', 'three', 'four']

        Args:
            index (int | slice): the desired index or slice to get.

        Returns:
            item (T | Sequence[T]): the item or items at index or slice. Items are of type T and slices are returned as list[T].
        
        Raises:
            IndexError: if the index is out of bounds.
            TypeError: if the index is not an integer or slice.
        """
        pass

    @abstractmethod
    def __setitem__(self, index: int, item: T) -> None:
        """ Bracket operator for setting an item in an Array.

        Examples:
            >>> array = Array[int](starting_sequence=[50], data_type=int)
            >>> array[0] = 10 # invokes __setitem__ with 0 as the index and 10 as the item to store at that index.
            >>> print(array[0]) 
            10
            >>> print(array) 
            [10]

        Args:
            index (int): the desired index to set.
            item (T): the desired item to set at index.
        
        Returns:
            None
        
        Raises: 
            IndexError: if the index is out of bounds.
            TypeError: if the item is not the same type as the Array.
        """
        pass

    @abstractmethod
    def append(self, data: T) -> None:
        """ Append an item to the end of the Array. Internally, the Array should manage a physical size (the size of the internal numpy array) 
            and a logical size (the number of items in the Array). The algorithm should double the array physical size when the number of items in the array (logical size) 
            is equal to the physical size.

        Examples:
            >>> array = Array[int](starting_sequence=[], data_type=int)
            >>> print(repr(array))
            Array(logical size: 0, items: [], physical size: 0, data type: <class 'int'>)
            >>> for i in range(10): 
            ...     array.append(i)
            ...     print(repr(array))
            Array(logical size: 0, items: [], physical size: 0, data type: <class 'int'>)
            Array(logical size: 1, items: [0], physical size: 2, data type: <class 'int'>)
            Array(logical size: 2, items: [0, 1], physical size: 2, data type: <class 'int'>)
            Array(logical size: 3, items: [0, 1, 2], physical size: 4, data type: <class 'int'>)
            Array(logical size: 4, items: [0, 1, 2, 3], physical size: 4, data type: <class 'int'>)
            Array(logical size: 5, items: [0, 1, 2, 3, 4], physical size: 8, data type: <class 'int'>)
            Array(logical size: 6, items: [0, 1, 2, 3, 4, 5], physical size: 8, data type: <class 'int'>)
            Array(logical size: 7, items: [0, 1, 2, 3, 4, 5, 6], physical size: 8, data type: <class 'int'>)
            Array(logical size: 8, items: [0, 1, 2, 3, 4, 5, 6, 7], physical size: 8, data type: <class 'int'>)
            Array(logical size: 9, items: [0, 1, 2, 3, 4, 5, 6, 7, 8], physical size: 16, data type: <class 'int'>)
            Array(logical size: 10, items: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], physical size: 16, data type: <class 'int'>)
    Args:
        data (T): the desired data to append.
    Returns:
        None
    """
        pass

    @abstractmethod
    def append_front(self, data: T) -> None:
        """ Append an item to the front of the Array. Internally, the Array should manage a physical size (the size of the internal numpy array) 
        and a logical size (the number of items in the Array). The algorithm should double the array physical size when the number of items in the array (logical size) 
        is equal to the physical size. 

        Examples:
            >>> array = Array[int](starting_sequence=[], data_type=int)
            >>> print(repr(array))
            Array(logical size: 0, items: [], physical size: 0, data type: <class 'int'>)
            >>> for num in range(10, 0, -1): 
            ...     array.append_front(i)
            ...     print(repr(array))
            Array(logical size: 1, items: [10], physical size: 2, data type: <class 'int'>)
            Array(logical size: 2, items: [9, 10], physical size: 2, data type: <class 'int'>)
            Array(logical size: 3, items: [8, 9, 10], physical size: 4, data type: <class 'int'>)
            Array(logical size: 4, items: [7, 8, 9, 10], physical size: 4, data type: <class 'int'>)
            Array(logical size: 5, items: [6, 7, 8, 9, 10], physical size: 8, data type: <class 'int'>)
            Array(logical size: 6, items: [5, 6, 7, 8, 9, 10], physical size: 8, data type: <class 'int'>)
            Array(logical size: 7, items: [4, 5, 6, 7, 8, 9, 10], physical size: 8, data type: <class 'int'>)
            Array(logical size: 8, items: [3, 4, 5, 6, 7, 8, 9, 10], physical size: 8, data type: <class 'int'>)
            Array(logical size: 9, items: [2, 3, 4, 5, 6, 7, 8, 9, 10], physical size: 16, data type: <class 'int'>)
            Array(logical size: 10, items: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], physical size: 16, data type: <class 'int'>)
            
        Args:
            data (T): the desired data to append.
        Returns:
            None
        """
        pass

    @abstractmethod
    def pop(self) -> None:
        """ 
        Pop an item from the end of the Array. Internally, the Array should manage a physical size (the size of the internal numpy array)
            and a logical size (the number of items in the Array). The algorithm should shrink the array physical size by half when the logical size is less than or equal to 1/4 of the physical size.
        
        Examples:
            >>> array = Array[int](starting_sequence=[num for num in range(10)], data_type=int)
            >>> print(repr(array))
            Array(logical size: 9 items: [0, 1, 2, 3, 4, 5, 6, 7, 8] physical size: 10, data type: <class 'int'>)
            >>> for i in range(10):
            ...     array.pop()
            ...     print(repr(array))
            Array(logical size: 8 items: [0, 1, 2, 3, 4, 5, 6, 7] physical size: 10, data type: <class 'int'>)
            Array(logical size: 7 items: [0, 1, 2, 3, 4, 5, 6] physical size: 10, data type: <class 'int'>)
            Array(logical size: 6 items: [0, 1, 2, 3, 4, 5] physical size: 10, data type: <class 'int'>)
            Array(logical size: 5 items: [0, 1, 2, 3, 4] physical size: 10, data type: <class 'int'>)
            Array(logical size: 4 items: [0, 1, 2, 3] physical size: 10, data type: <class 'int'>)
            Array(logical size: 3 items: [0, 1, 2] physical size: 10, data type: <class 'int'>)
            Array(logical size: 2 items: [0, 1] physical size: 5, data type: <class 'int'>)
            Array(logical size: 1 items: [0] physical size: 2, data type: <class 'int'>)
            Array(logical size: 0 items: [] physical size: 1, data type: <class 'int'>)

        Returns:
            None
        """
        pass
    
    @abstractmethod
    def pop_front(self) -> None:
        """ 
        Pop an item from the front of the Array. Internally, the Array should manage a physical size (the size of the internal numpy array)
        and a logical size (the number of items in the Array). The algorithm should shrink the array physical size by half when the logical size is less than or equal to 1/4 of the physical size.

        Examples:
            >>> array = Array[int](starting_squence[num for num in range(10)], data_type=int)
            >>> print(repr(array))
            Array(logical size: 9 items: [0, 1, 2, 3, 4, 5, 6, 7, 8] physical size: 10, data type: <class 'int'>)
            >>> for i in range(10):
            ...     array.pop_front()
            ...     print(repr(array))
            Array(logical size: 8 items: [1, 2, 3, 4, 5, 6, 7, 8] physical size: 10, data type: <class 'int'>)
            Array(logical size: 7 items: [2, 3, 4, 5, 6, 7, 8] physical size: 10, data type: <class 'int'>)
            Array(logical size: 6 items: [3, 4, 5, 6, 7, 8] physical size: 10, data type: <class 'int'>)
            Array(logical size: 5 items: [4, 5, 6, 7, 8] physical size: 10, data type: <class 'int'>)
            Array(logical size: 4 items: [5, 6, 7, 8] physical size: 10, data type: <class 'int'>)
            Array(logical size: 3 items: [6, 7, 8] physical size: 10, data type: <class 'int'>)
            Array(logical size: 2 items: [7, 8] physical size: 5, data type: <class 'int'>)
            Array(logical size: 1 items: [8] physical size: 2, data type: <class 'int'>)
            Array(logical size: 0 items: [] physical size: 1, data type: <class
        Returns:
            None

        Raises:
            IndexError: if the Array is empty.
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """ Length operator for getting the logical length (size) of the Array (number of items in the Array).

        Examples:
            >>> array = Array[int](starting_sequence=[num for num in range(10)], data_type=int)
            >>> print(len(array))
            10

        Returns:
            length (int): the length of the Array.
        """
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """ Equality operator == to check if two Arrays are equal (deep check).

        Examples:
            >>> array1 = Array[int](starting_sequence=[0, 1, 2, 3, 4], data_type=int)
            >>> array2 = Array[int](starting_sequence=[0, 1, 2, 3, 4], data_type=int)
            >>> print(array1 == array2)
            True
            array3 = Array[int](starting_sequence=[0, 1, 2, 3, 5], data_type=int)
            >>> print(array1 == array3)
            False

        Args:
            other (object): the instance to compare self to.
        
        Returns:
            is_equal (bool): true if the arrays are equal (deep check).
        """
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[T]:
        """ Iterator operator. Allows for iteration over the Array.
        Examples:
            >>> array = Array[str](starting_sequence=['one', 'two', 'three', 'four', 'five'], data_type=str)
            >>> for item in array: # invokes __iter__
            ...     print(repr(str(item)), end= ' ') 
            'one' 'two' 'three' 'four' 'five'

        Yields:
            item (T): yields the item at index
        """
        pass

    @abstractmethod
    def __reversed__(self) -> Iterator[T]:
        """ Reversed iterator operator. Allows for iteration over the Array in reverse.
        Examples:
            >>> array = Array[str](starting_sequence=['one', 'two', 'three', 'four', 'five'], data_type=str)
            >>> for item in reversed(array):
            ...     print(repr(str(item)), end= ' ')
            'five' 'four' 'three' 'two' 'one'

        Yields:
            item (T): yields the item at index starting at the end
        """
        pass

    @abstractmethod
    def __delitem__(self, index: int) -> None:
        """ Delete an item in the array. Copies the array contents from index + 1 down
            to fill the gap caused by deleting the item and shrinks the array size down by one.
            The algorithm should shrink the array physical size when the number of items in the array (logical size) is less than or 
            equal to 1/4 of the physical size.

        Examples:
            >>> array = Array[str](starting_sequence=['zero', 'one', 'two', 'three', 'four'], data_type=str)
            >>> print(repr(array))
            Array(logical size: 5, items: ['zero', 'one', 'two', 'three', 'four'], physical size: 5, data type: <class 'str'>)
            >>> del array[2]
            >>> print(repr(array))
            Array(logical size: 4, items: ['zero', 'one', 'three', 'four'], physical size: 5, data type: <class 'str'>)

        Args:
            index (int): the desired index to delete.
        
        Returns:
            None
        """
        pass

    @abstractmethod
    def __contains__(self, item: Any) -> bool:
        """ Contains operator (in). Checks if the array contains the item.

        Examples:
            >>> array = Array[str](starting_sequence=['zero', 'one', 'two', 'three', 'four'], data_type=str)
            >>> print('three' in array)
            True
            >>> print('five' in array)
            False
            
        Args:
            item (Any): the desired item to check whether it's in the array.

        Returns:
            contains_item (bool): true if the array contains the item.
        """
        pass

    @abstractmethod
    def clear(self) -> None:
        """ Clear the Array
        
        Examples:
            >>> array = Array[int](starting_sequence=[num for num in range(10)], data_type=int)
            >>> print(repr(array))
            Array(logical size: 10, items: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], physical size: 10, data type: <class 'int'>)
            >>> array.clear()
            >>> print(repr(array))
            Array(logical size: 0, items: [], physical size: 10, data type: <class 'int'>)
            
        Returns:
            None
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """ Return a string representation of the data and structure. 

        Examples:
            >>> array = Array[int](starting_sequence=[num for num in range(10)], data_type=int)
            >>> print(str(array))
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            >>> array = Array[str](starting_sequence=['zero', 'one', 'two', 'three', 'four'], data_type=str)
            >>> print(str(array)))
            [zero, one, two, three, four]
        
        Returns:
            string (str): the string representation of the data and structure.
        """
        pass
    
    @abstractmethod
    def __repr__(self) -> str:
        """ Return a programmer's representation of the data and structure.
        
        Examples:
            >>> array = Array[int](starting_sequence=[num for num in range(10)], data_type=int)
            >>> print(repr(array))
            Array(logical size: 10, items: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], physical size: 10, data type: <class 'int'>)
            >>> array = Array[str](starting_sequence=['zero', 'one', 'two', 'three', 'four'], data_type=str)
            >>> print(repr(array))
            Array(logical size: 5, items: ['zero', 'one', 'two', 'three', 'four'], physical size: 5, data type: <class 'str'>)
        
        Returns:
            string (str): the programmer's representation of the data and structure.
        """
        pass


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
