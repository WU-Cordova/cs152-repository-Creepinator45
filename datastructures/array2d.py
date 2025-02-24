from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int) -> None:
            raise NotImplementedError('Row.__init__ not implemented.')

        def __getitem__(self, column_index: int) -> T:
            raise NotImplementedError('Row.__getitem__ not implemented.')
        
        def __setitem__(self, column_index: int, value: T) -> None:
            raise NotImplementedError('Row.__setitem__ not implemented.')
        
        def __iter__(self) -> Iterator[T]:
            raise NotImplementedError('Row.__iter__ not implemented.')
        
        def __reversed__(self) -> Iterator[T]:
            raise NotImplementedError('Row.__reversed__ not implemented.')

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        raise NotImplementedError('Array2D.__init__ not implemented.')

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        raise NotImplementedError('Array2D.empty not implemented.')

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        raise NotImplementedError('Array2D.__getitem__ not implemented.')
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        raise NotImplementedError('Array2D.__iter__ not implemented.')
    
    def __reversed__(self):
        raise NotImplementedError('Array2D.__reversed__ not implemented.')
    
    def __len__(self): 
        raise NotImplementedError('Array2D.__len__ not implemented')
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.__num_rows} Rows x {self.__num_columns} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')