import os
from datastructures.istack import IStack
from typing import Generic

from datastructures.linkedlist import LinkedList

class ListStack[T](Generic[T], IStack[T]):
    """
    ListStack (LinkedList-based Stack)

    """

    def __init__(self, data_type:object) -> None:
        """
        Initializes the ListStack.

        Args:
            data_type (type): The type of data the stack will hold.

        """
        raise NotImplementedError("ListStack.__init__ is not implemented.")

    def push(self, item: T):
        """
        Pushes an item onto the stack.

        Args:
            item (T): The item to push onto the stack.
        
        Raises:
            TypeError: If the item is not of the correct type.

        """
        raise NotImplementedError("ListStack.push is not implemented.")

    def pop(self) -> T:
        """
        Removes and returns the top item from the stack.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        raise NotImplementedError("ListStack.pop is not implemented.")

    def peek(self) -> T:
        """
        Returns the top item from the stack without removing it.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        raise NotImplementedError("ListStack.peek is not implemented.")

    @property
    def empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        raise NotImplementedError("ListStack.empty is not implemented.")

    def clear(self):
        """
        Clears all items from the stack.
        """
        raise NotImplementedError("ListStack.clear is not implemented.")

    def __contains__(self, item: T) -> bool:
        """
        Checks if an item exists in the stack.

        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item exists in the stack, False otherwise.

        """
        raise NotImplementedError("ListStack.__contains__ is not implemented.")

    def __eq__(self, other) -> bool:
        """
        Compares two stacks for equality.

        Args:
            other (ListStack): The stack to compare with.

        Returns:
            bool: True if the stacks are equal, False otherwise.

        """
        raise NotImplementedError("ListStack.__eq__ is not implemented.")

    def __len__(self) -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        raise NotImplementedError("ListStack.__len__ is not implemented.")

    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
        raise NotImplementedError("ListStack.__str__ is not implemented.")

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the stack.

        Returns:
            str: A detailed string representation of the stack.

        """
        raise NotImplementedError("ListStack.__repr__ is not implemented.")
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
