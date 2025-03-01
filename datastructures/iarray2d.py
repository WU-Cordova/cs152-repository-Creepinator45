""" This module defines an Array2D interface that represents a two-dimensional array. 
    This file lists the stipulations and more information on the methods and their expected behavior.
    YOU SHOULD NOT MODIFY THIS FILE.
    Implement the Array2D class in the array2d.py file.
"""

from __future__ import annotations
from collections.abc import Sequence

from abc import ABC, abstractmethod
from typing import Any, Generic, Iterator, TypeVar

from datastructures.iarray import IArray

T = TypeVar('T', bound=Any)


class IArray2D(Generic[T], ABC):
    """ An interface that represents the minimal functions needed to make an Array object
        into a two-dimensional array. Other typical functions like str, len, repr, etc. are not
        included in this interface because they are provided by the IArray
    """
    class IRow(Generic[T], ABC):
        """ An interface that represents a row in a two-dimensional array in order to support
            iteration and indexing. This class is not intended to be used directly by a user, 
            but rather as a helper class for the Array2D to provide the second bracket operator.
        """
        @abstractmethod
        def __init__(self, row_index: int, array: IArray, num_columns: int) -> None:
            """ Initializes the Row object. 
            
            Args:
                row_index (int): The index of the row in the two-dimensional array.
                array (IArray): The two-dimensional array that the row belongs to.
                num_columns (int): The number of columns in the row.
            """
            ... 

        @abstractmethod
        def __getitem__(self, column_index: int) -> T:
            """ Gets the item at the specified column index in the row. This method is intended to be used
                by the Array2D class to provide the second bracket operator. """
            ...

        @abstractmethod
        def __setitem__(self, column_index: int, value: T) -> None:
            """ Sets the item at the specified column index in the row. This method is intended to be used
                by the Array2D class to provide the second bracket operator. """
            ...
        
        @abstractmethod
        def __iter__(self) -> Iterator[T]:
            """ Returns an iterator of the row. 
        
            Returns:
                Iterator[T]: An iterator of the row.
            """
            ...
        
        @abstractmethod
        def __reversed__(self) -> Iterator[T]:
            """ Returns a reverse iterator of the row. 
        
            Returns:
                Iterator[T]: A reverse iterator of the row.
            """
            ...
        
        @abstractmethod
        def __len__(self) -> int:
            """ Returns the number of columns in the row.
        
            Returns:
                int: The number of columns in the row.
            """
            ...

    @abstractmethod
    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None: 
        """ Initializes the Array2D object with a starting sequence of sequences.

        Examples:
            >>> array2d = Array2D([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            >>> repr(array2d)
            Array2D [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            >>> 
        
        Args:
            starting_sequence (Sequence[Sequence[T]]): The starting sequence of sequences (default: [[]]).
            data_type (type): The type of data that the array will hold (default: object).
            
        Raises:
            ValueError: If the starting sequence is not a valid sequence.
            ValueError: If the starting sequence is not a sequence of sequences.
            TypeError: If all items are not of the same type.

        Returns:
            None            
            """
        ...

    @staticmethod
    @abstractmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> IArray2D[T]: 
        """ Creates an empty two-dimensional array with the specified number of rows and columns.
        
        Args:
            rows (int): The number of rows in the two-dimensional array (default: 0).
            cols (int): The number of columns in the two-dimensional array (default: 0).
            data_type (type): The type of data that the array will hold (default: object).
        
        Returns:
            IArray2D[T]: An empty two-dimensional array of the specified size and data type.
        """
        ...

    @abstractmethod
    def __getitem__(self, index: int) -> IRow[T]: 
        """ Gets the item at the specified index or a slice of the two-dimensional array. If the index is a slice,
            the method should return an IArray2D with the specified slice of the two-dimensional array. 
            Otherwise, it should return an array at the specified index since the elements of the two-dimensional array
            are arrays.
        Args:
            index (int | slice): The index or slice of the two-dimensional array.
            
        Returns:
            IArray[T] | IArray2D[T]: The item at the specified index or a slice of the two-dimensional array.
            
        Raises:
            IndexError: If the index is out of bounds.
            
        """
        ...

    @abstractmethod
    def __iter__(self) -> Iterator[Sequence[T]]:
        """ Returns an iterator of the two-dimensional array. Because the two dimensional array is an IArray,
            this method should return an iterator to the IArray.
        
        Returns:
            Iterator[IArray[T]]: An iterator of the two-dimensional array.
        """
        ...

    @abstractmethod
    def __reversed__(self) -> Iterator[Sequence[T]]:
        """ Returns an iterator of the two"""

    @abstractmethod
    def __len__(self) -> int:
        """ Returns the number of rows in the two-dimensional array.
        
        Returns:
            int: The number of rows in the two-dimensional array.
        """

    @abstractmethod
    def __str__(self) -> str:
        """ Returns a string representation of the two-dimensional array. The string representation
            should include the string representation of each array in the two-dimensional array.
        
        Returns:
            str: A string representation of the two-dimensional array.
        """
        ...

    @abstractmethod
    def __repr__(self) -> str:
        """ Returns a string representation of the two-dimensional array. The string representation
            should include the string representation of each array in the two-dimensional array.
        
        Returns:
            str: A string representation of the two-dimensional array.
        """
        ...
