from __future__ import annotations
import os
from typing import Iterator, Sequence
import numpy as np

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int) -> None:
            self.row_index = row_index
            self.array = array
            self.num_columns = num_columns

        def __getitem__(self, column_index: int) -> T:
            if column_index >= self.num_columns:
                raise IndexError("column index out of bounds")
            #idk why using the static method requires accounting for name mangling like this, and I don't care to figure it out right now
            return self.array[Array2D._Array2D__mapIndex2d(self.num_columns, self.row_index, column_index)]
        
        def __setitem__(self, column_index: int, value: T) -> None:
            self.array[Array2D._Array2D__mapIndex2d(self.num_columns, self.row_index, column_index)] = value
        
        def __iter__(self) -> Iterator[T]:
            for i in range(self.num_columns):
                yield self[i]
        
        def __reversed__(self) -> Iterator[T]:
            for i in range(self.num_columns-1, -1 ,-1):
                yield self[i]

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("starting_sequence not a sequence")
        if not isinstance(starting_sequence[0], Sequence):
            raise ValueError("starting_sequence not a sequence of sequences")
        if isinstance(starting_sequence, str):
            raise ValueError("starting_sequence is a string, not a sequence of sequences")
        
        self.__data_type = data_type
        self.__num_rows = len(starting_sequence)
        self.__num_columns = len(starting_sequence[0])

        for row in starting_sequence:
            if not isinstance(row, Sequence):
                raise ValueError("starting_sequence not a sequence of sequences")
            if len(row) != self.__num_columns:
                raise ValueError("rows in starting sequence have inconsistent lengths")
            for item in row:
                if not isinstance(item, self.__data_type):
                    raise ValueError("items in starting_sequence are not of type data_type")

        self.__elements2d = Array(starting_sequence=[data_type() for _ in range(self.__num_rows * self.__num_columns)], data_type=data_type)
        #I thought about doing this in a single for loop, by looping through __elements2d and using itertools.permutations to iterate through all indices of starting sequence, but I think this should be more efficient since it directly accesses the iterator for the row rather than having to look up both indeces in sequence for each item assignment
        for i, row in enumerate(starting_sequence):
            for j, item in enumerate(row):
                self.__elements2d[Array2D.__mapIndex2d(self.__num_columns, i, j)] = item

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        #my init implementation already creates an empty array before setting the values, so doing it this way makes it loop through and set each value to what it already is
        #incredibly redundant and inefficient, I don't care to figure out a way to fix it right now tho
        emptyStartingSequence = [[data_type() for _ in range(cols)] for _ in range(rows)]
        return Array2D(emptyStartingSequence, data_type=data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        if row_index >= self.__num_rows:
            raise IndexError("row index out of bounds")
        return self.Row(row_index, self.__elements2d, self.__num_columns)
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        #I could maybe do this more efficiently by making use of Array's iter implementation, which uses numpy's iter implementation, but idc. This array2D implementation is already pointless and inefficient compared to numpy anyway
        for i in range(self.__num_rows):
            yield self[i]
    
    def __reversed__(self):
        for i in range(self.__num_rows-1, -1, -1):
            yield self[i]
    
    def __len__(self): 
        return self.__num_rows
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.__num_rows} Rows x {self.__num_columns} Columns, items: {str(self)}'
    
    @staticmethod
    def __mapIndex2d(cols_len, row_index: int, col_index: int) -> int:
        """
        maps 2d index onto flattened array2d, sliced by rows
        """
        if col_index < 0:
            row_index += 1
        return row_index * cols_len + col_index


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')