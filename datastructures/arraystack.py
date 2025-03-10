import os

from datastructures.array import Array, T
from datastructures.istack import IStack

class ArrayStack(IStack[T]):
    ''' ArrayStack class that implements the IStack interface. The ArrayStack is a 
        fixed-size stack that uses an Array to store the items.'''
    
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        ''' Constructor to initialize the stack 
        
            Arguments: 
                max_size: int -- The maximum size of the stack. 
                data_type: type -- The data type of the stack.       
        '''
        raise NotImplementedError('ArrayStack is not implemented')

    def push(self, item: T) -> None:
        raise NotImplementedError

    def pop(self) -> T:
       raise NotImplementedError

    def clear(self) -> None:
       raise NotImplementedError
    @property
    def peek(self) -> T:
       raise NotImplementedError

    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the stack. 
        
            Returns:
                int: The maximum size of the stack.
        '''
        raise NotImplementedError    
    @property
    def full(self) -> bool:
        ''' Returns True if the stack is full, False otherwise. 
        
            Returns:
                bool: True if the stack is full, False otherwise.
        '''
        raise NotImplementedError

    @property
    def empty(self) -> bool:
        raise NotImplementedError
    def __eq__(self, other: object) -> bool:
       raise NotImplementedError

    def __len__(self) -> int:
       raise NotImplementedError
    
    def __contains__(self, item: T) -> bool:
       raise NotImplementedError

    def __str__(self) -> str:
        return str([self.stack[i] for i in range(self._top)])
    
    def __repr__(self) -> str:
        return f"ArrayStack({self.maxsize}): items: {str(self)}"
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')

