import os

from datastructures.array import Array, T
from datastructures.istack import IStack
from copy import deepcopy

class ArrayStack(IStack[T]):
    ''' ArrayStack class that implements the IStack interface. The ArrayStack is a 
        fixed-size stack that uses an Array to store the items.'''
    
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        ''' Constructor to initialize the stack 
        
            Arguments: 
                max_size: int -- The maximum size of the stack. 
                data_type: type -- The data type of the stack.       
        '''
        self.__top = -1
        self.__stack = Array([data_type()]*max_size, data_type=data_type)

    def push(self, item: T) -> None:
        self.__top += 1
        self.__stack[self.__top] = item

    def pop(self) -> T:
        if self.empty:
            raise IndexError
        topItem = self.peek
        self.__top -= 1
        return topItem

    def clear(self) -> None:
        self.__top = -1

    @property
    def peek(self) -> T:
        if self.empty:
            raise IndexError
        return self.__stack[self.__top]

    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the stack. 
        
            Returns:
                int: The maximum size of the stack.
        '''
        return len(self.__stack) 
    @property
    def full(self) -> bool:
        ''' Returns True if the stack is full, False otherwise. 
        
            Returns:
                bool: True if the stack is full, False otherwise.
        '''
        return self.__top+1 == self.maxsize

    @property
    def empty(self) -> bool:
        return self.__top == -1
    
    def __eq__(self, other: object) -> bool:
        if len(self) != len(other):
            return False
        #should I be making a deepcopy of self as well?
        other_copy = deepcopy(other)
        #slicing our array type is inefficient, this could be made more efficient by avoiding doing that
        for item in reversed(self.__stack[0:self.__top+1]):
            if item != other_copy.pop():
                return False
        return True

    def __len__(self) -> int:
        return self.__top+1
    
    def __contains__(self, item: T) -> bool:
        #slicing our array type is inefficient, so this could be made more efficient but less readable by writing contains from scratch rather than leveraging our array type's contains function
        return item in self.__stack[0:self.__top]

    def __str__(self) -> str:
        return str([self.__stack[i] for i in range(len(self))])
    
    def __repr__(self) -> str:
        return f"ArrayStack({self.maxsize}): items: {str(self)}"
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')

