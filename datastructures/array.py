# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray
from copy import deepcopy

from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        """
        init array
        O(n) operation for length of starting_sequence
        """
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("starting_sequence must be a valid sequence type")
        if not isinstance(data_type, type):
            raise ValueError("data_type must be a type")

        self.__item_count: int = len(starting_sequence)
        self.__capacity: int = self.__item_count
        self.__data_type: type = data_type

        self.__items: NDArray = np.empty(self.__capacity, dtype = self.__data_type)

        for i, item in enumerate(starting_sequence):
            #__setitem__ handles individual item error checking
            self[i] = item
    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        """
        get item from array
        O(n) operation for length of return sequence
        """
        if isinstance(index, slice):
            #index checking and setting defaults
            start = 0 if index.start is None else index.start
            #start = index.start
            if not (start is None or self.__in_range(start)): #shortcircuited or means that self.__in_range won't raise error if index is None
                raise IndexError(f"Start index {start} out of bounds. Array length is {self.__item_count}")
            
            stop = self.__item_count if index.stop is None else index.stop
            #stop = index.stop
            if not (stop is None or self.__in_range(stop-1)): #shortcircuited or means that self.__in_range won't raise error if index is None
                raise IndexError(f"Stop index {stop} out of bounds. Array length is {self.__item_count}")
            
            step = 1 if index.step is None else index.step
            #step = index.step
            if not (step is None or self.__in_range(step)): #shortcircuited or means that self.__in_range won't raise error if index is None
                raise IndexError(f"Step index {step} out of bounds. Array length is {self.__item_count}")

            sliced_items = self.__items[start:stop:step]
            #surely there's a better way to do this... creating a entirely new array to return -- complete with deep copies of all the data -- seems wasteful. Maybe I'm spoiled from Rust's slices...
            #iirc, doing this kind of slicing on a numpy array directly is O(1), and almost free. So implementing our own slice function in this way is way slower
            return Array(starting_sequence=sliced_items.tolist(), data_type=self.__data_type)
        
        elif isinstance(index, int):
            if not self.__in_range(index):
                raise IndexError(f"Index {index} out of bounds. Array length is {self.__item_count}")
            
            item = self.__items[index]
            return item.item() if isinstance(item, np.generic) else item
        
        else:
            raise TypeError(f"invalid index, not an int or slice")
    
    def __setitem__(self, index: int, item: T) -> None:
        """
        set item in array
        O(1) operation
        """
        if not isinstance(item, self.__data_type):
            raise TypeError(f"item {item} of type {type(item)} not of type {self.__data_type}")
        if not self.__in_range(index):
            raise IndexError(f"Index {index} out of bounds. Array length is {self.__item_count}")
        
        self.__items[index] = deepcopy(item)

    def append(self, data: T) -> None:
        """
        append to end of array
        ammortized O(1) operation
        """
        if self.__capacity >= self.__item_count:
            self.__resize(self.__capacity * 2)
        self.__item_count += 1
        #__setitem__ handles type checking
        #doing error checking after increasing __item_count lets me reuse the __setitem__ function
        #could cause a problematic desync in the event of the program continuing after an error. Only matters if the end user catches the error
        self[-1] = data

    def append_front(self, data: T) -> None:
        """
        append to front of array
        O(n) operation for size of array
        """
        #this setup is horribly inefficient
        #I should rewrite this to shift items over in the same step as resizing if possible
        #Is there a way to avoid having to shift all items over every append_front()?
        #grow if needed
        if self.__capacity >= self.__item_count:
            self.__grow(self.__capacity * 2)
        self.__item_count += 1
        #shift elements to the right
        for i, item in enumerate(reversed(self), start=1):
            #setting items using public method includes unnecessary error checking. Could increase efficiency by setting items directly
            #also, setting items using public method potentially performs unnecessary deep copying
            self[-i] = item
        #set data
        #__setitem__ handles type checking
        #doing error checking after preamble lets me reuse the __setitem__ function
        #could cause a problematic desync in the event of the program continuing after an error. Only matters if the end user catches the error
        self[0] = data

    def pop(self) -> None:
        del self[-1]
    
    def pop_front(self) -> None:
        del self[0]

    def __len__(self) -> int: 
        """
        return logical size
        O(1) operation
        """
        return self.__item_count

    def __eq__(self, other: object) -> bool:
        """
        check equivalence
        O(n) operation for length of array
        """
        if not isinstance(other, Array):
            return False
        if len(other) != len(self):
            return False
        
        items_eq = True
        #todo, change this to makes use of __iter__ when it's implemented
        for item_o, item_s in zip(other, self):
            items_eq = items_eq and (item_o == item_s)
        return items_eq

    def __iter__(self) -> Iterator[T]:
        """
        numpy iterator wrapper
        O(1) operation
        """
        iterator = iter(self.__items[0:self.__item_count])
        for item in iterator:
            yield item.item() if isinstance(item, np.generic) else item

    def __reversed__(self) -> Iterator[T]:
        """
        uses __iter__ on a reversed array
        O(n) operation for length of array
        """
        #this hacky code I wrote makes me upset
        #I would ideally just use self[::-1] to reverse it, but this doesn't work with the way defaults are set in the slice
        #It also seems incredibly wasteful to create an entirely new array to feed into __iter__, when slicing into a numpy array directly is so costless
        return iter(Array(starting_sequence=self.__items[self.__item_count-1::-1].tolist(), data_type=self.__data_type))

    def __delitem__(self, index: int) -> None:
        """
        delete item from array
        O(n) operation for length of array-index
        """
        if not self.__in_range(index):
            raise IndexError(f"Index {index} out of bounds. Array length is {self.__item_count}")
        
        for i, item in enumerate(self[index+1:], index+1):
            #setting items using public method potentially performs unnecessary deep copying. This should maybe be rewritten to set values directly
            self[i-1] = item
        self.__item_count -= 1

        if self.__item_count <= self.__capacity/4:
            self.__resize(int(self.__capacity/2))

    def __contains__(self, item: Any) -> bool:
        """
        uses numpy __contains__
        O(n) operation for length of array?
        """
        return item in self.__items

    def clear(self) -> None:
        """
        sets items to a new numpy array
        sets capacity to 1 and item count to 0
        O(1) operation
        """
        self.__items = np.empty(1, dtype=self.__data_type)
        self.__capacity = 1
        self.__item_count = 0

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__item_count}, Physical: {len(self.__items)}, type: {self.__data_type}'
    
    def __in_range(self, index: int) -> bool:
        return -self.__item_count <= index < self.__item_count
    
    def __resize(self, new_size: int) -> None:
        """
        resizes array using numpy.resize
        O(n) operation for new length of array
        """
        if new_size <= self.__item_count:
            raise ValueError("attempted to set capacity smaller than item_count")
        self.__capacity = new_size
        self.__items.resize(new_size)

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')