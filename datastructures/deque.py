import os
from datastructures.iqueue import IQueue
from datastructures.linkedlist import LinkedList
from typing import TypeVar

T = TypeVar('T')

class Deque[T](IQueue[T]):
    """
    A double-ended queue (deque) implementation.
    """

    def __init__(self, data_type: type = object) -> None:
        """
        Initializes the deque with a specified data type.

        Args:
            - data_type (type): The type of data the deque will hold.
        """
        raise NotImplementedError("Deque initialization is not implemented.")

    def enqueue(self, item: T) -> None:
        """
        Adds an item to the back of the deque.

        Args:
            - item (T): The item to add to the back of the deque.

        Raises:
            - TypeError: If the item is not of the correct type.
        """
        raise NotImplementedError("Method to add an item to the back of the deque is not implemented.")

    def dequeue(self) -> T:
        """
        Removes and returns the item from the front of the deque.

        Returns:
            - T: The item removed from the front of the deque.

        Raises:
            - IndexError: If the deque is empty.
        """
        raise NotImplementedError("Method to remove an item from the front of the deque is not implemented.")

    def enqueue_front(self, item: T) -> None:
        """
        Adds an item to the front of the deque.

        Args:
            - item (T): The item to add to the front of the deque.

        Raises:
            - TypeError: If the item is not of the correct type.
        """
        raise NotImplementedError("Method to add an item to the front of the deque is not implemented.")

    def dequeue_back(self) -> T:
        """
        Removes and returns the item from the back of the deque.

        Returns:
            - T: The item removed from the back of the deque.

        Raises:
            - IndexError: If the deque is empty.
        """
        raise NotImplementedError("Method to remove an item from the back of the deque is not implemented.")

    def front(self) -> T:
        """
        Returns the front item of the deque without removing it.

        Returns:
            - T: The front item of the deque.

        Raises:
            - IndexError: If the deque is empty.
        """
        raise NotImplementedError("Method to get the front item of the deque is not implemented.")

    def back(self) -> T:
        """
        Returns the back item of the deque without removing it.

        Returns:
            - T: The back item of the deque.

        Raises:
            - IndexError: If the deque is empty.
        """
        raise NotImplementedError("Method to get the back item of the deque is not implemented.")

    def empty(self) -> bool:
        """
        Checks if the deque is empty.

        Returns:
            - bool: True if the deque is empty, False otherwise.
        """
        raise NotImplementedError("Method to check if the deque is empty is not implemented.")

    def __len__(self) -> int:
        """
        Returns the number of items in the deque.

        Returns:
            - int: The number of items in the deque.
        """
        raise NotImplementedError("Method to get the length of the deque is not implemented.")
    
    def __contains__(self, item: T) -> bool:
        """
        Checks if an item exists in the deque.

        Args:
            - item (T): The item to check for existence.

        Returns:
            - bool: True if the item exists in the deque, False otherwise.
        """
        raise NotImplementedError("Method to check if an item exists in the deque is not implemented.")
    
    def __eq__(self, other) -> bool:
        """
        Compares two deques for equality.

        Args:
            - other (Deque): The deque to compare with.

        Returns:
            - bool: True if the deques are equal, False otherwise.
        """
        raise NotImplementedError("Method to compare two deques is not implemented.")
    
    def clear(self):
        """
        Clears all items from the deque.
        """
        raise NotImplementedError("Method to clear the deque is not implemented.")

    def __str__(self) -> str:
        """
        Returns a string representation of the deque.

        Returns:
            - str: A string representation of the deque.
        """
        raise NotImplementedError("Method to get the string representation of the deque is not implemented.")
    
    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the deque.

        Returns:
            - str: A detailed string representation of the deque.
        """
        raise NotImplementedError("Method to get the detailed string representation of the deque is not implemented.")


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
