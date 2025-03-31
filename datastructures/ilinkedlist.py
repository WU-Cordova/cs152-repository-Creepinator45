from __future__ import annotations
from abc import abstractmethod
import abc
import os
from typing import Sequence, TypeVar

T = TypeVar('T')

class ILinkedList[T](abc.ABC):

    '''The `ILinkedList` interface defines a set of methods that a linked list data structure 
        should implement. This interface is designed to be generic, allowing it to work with any data type. 
        Below is a detailed explanation of each method in the interface.
    '''

    @abstractmethod
    def __init__(self, data_type: type = object) -> None:

        ''' Initializes the LinkedList object with a data_type.

            Examples:
                >>> linked_list = LinkedList(data_type=int)
                >>> print(linked_list)
                ()
        
            Arguments:
                data_type: The type of the elements in the list
        '''
        ...
    
    @staticmethod
    @abstractmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> ILinkedList[T]:

        ''' Creates a LinkedList object from a Python list.

            Examples:
                >>> linked_list = LinkedList.from_sequence([1, 2, 3, 4, 5])
                >>> print(linked_list)
                (1 <-> 2 <-> 3 <-> 4 <-> 5)
        
            Arguments:
                sequence: The sequence to create the LinkedList from
                data_type: The data type of the items

            Returns:
                A LinkedList object

            Raises:
                TypeError: If the sequence contains elements not of the specified data type
            
        '''
        ...

    @abstractmethod
    def append(self, item: T) -> None:

        ''' Adds an item to the end of the list 
        
            Examples:
                >>> linked_list = LinkedList(data_type=int)
                >>> for i in range(10):
                ...     linked_list.append(i)
                >>> print(linked_list)
                (0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 <-> 8 <-> 9)
                
            Arguments:
                item: The item to add to the list

            Raises:
                TypeError: If the item is not of the correct type
            
        '''      
        ...

    @abstractmethod
    def prepend(self, item: T) -> None:

        ''' Adds an item to the beginning of the list
        
            Examples:
                >>> linked_list = LinkedList(data_type=int)
                >>> for i in range(10):
                ...     linked_list.prepend(i)
                >>> print(linked_list)
                (9 <-> 8 <-> 7 <-> 6 <-> 5 <-> 4 <-> 3 <-> 2 <-> 1 <-> 0)
                
            Arguments:
                item: The item to add to the list

            Raises:
                TypeError: If the item is not of the correct type
        '''
        ...

    @abstractmethod
    def insert_before(self, target: T, item: T) -> None:

        ''' Adds an item before the first occurrence of a target item
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> linked_list.append('dog')
                >>> linked_list.append('cat')
                >>> linked_list.insert_before('cat', 'mouse')
                >>> print(linked_list)
                (dog <-> mouse <-> cat)
                
            Arguments:
                target: The target item to insert before
                item: The item to add to the list

            Raises:
                TypeError: If the item or target is not of the correct type
                ValueError: If the target item is not in the list
        '''
        ...

    @abstractmethod
    def insert_after(self, target: T, item: T) -> None:

        ''' Adds an item after the first occurrence of a target item
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> linked_list.append('dog')
                >>> linked_list.append('cat')
                >>> linked_list.insert_after('dog', 'mouse')
                >>> print(linked_list)
                (dog <-> mouse <-> cat)
                
            Arguments:
                target: The target item to insert after
                item: The item to add to the list

            Raises:
                TypeError: If the item or target is not of the correct type
                ValueError: If the target item is not in the list
        '''
    ...

    @abstractmethod
    def remove(self, item: T) -> None:

        ''' Removes the first occurrence of an item from the list
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> linked_list.append('dog')
                >>> linked_list.append('cat')
                >>> linked_list.append('mouse')
                >>> linked_list.remove('cat')
                >>> print(linked_list)
                (dog <-> mouse)
                
            Arguments:
                item: The item to remove from the list

            Raises:
                TypeError: If the item is not of the correct type
                ValueError: If the item is not in the list
        '''
        ...

    @abstractmethod
    def remove_all(self, item: T) -> None:

        ''' Removes all occurrences of an item from the list
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> linked_list.append('dog')
                >>> linked_list.append('cat')
                >>> linked_list.append('mouse')
                >>> linked_list.append('cat')
                >>> linked_list.remove_all('cat')
                >>> print(linked_list)
                (dog <-> mouse)
                
            Arguments:
                item: The item to remove from the list

            Raises:
                TypeError: If the item is not of the correct type
        '''
        ...

    @abstractmethod
    def pop(self) -> T:

        ''' Removes and returns the last item in the list
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> linked_list.append('dog')
                >>> linked_list.append('cat')
                >>> linked_list.append('mouse')
                >>> linked_list.pop()
                'mouse'
                >>> print(linked_list)
                (dog <-> cat)
                
            Returns:
                The last item in the list

            Raises:
                IndexError: If the list is empty
        '''
        ...

    @abstractmethod
    def pop_front(self) -> T:

        ''' Removes and returns the first item in the list
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> linked_list.append('dog')
                >>> linked_list.append('cat')
                >>> linked_list.append('mouse')
                >>> linked_list.pop_front()
                'dog'
                >>> print(linked_list)
                (cat <-> mouse)
                
            Returns:
                The first item in the list

            Raises:
                IndexError: If the list is empty
        '''
        ...

    @property
    @abstractmethod
    def front(self) -> T:
        
        ''' Returns the first item in the list
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> linked_list.append('dog')
                >>> linked_list.append('cat')
                >>> linked_list.append('mouse')
                >>> linked_list.front
                ('dog')
                
            Returns:
                The first item in the list

            Raises:
                IndexError: If the list is empty
        '''
        ...

    @property
    @abstractmethod
    def back(self) -> T:

        ''' Returns the last item in the list
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> linked_list.append('dog')
                >>> linked_list.append('cat')
                >>> linked_list.append('mouse')
                >>> linked_list.back
                ('mouse')
                
            Returns:
                The last item in the list

            Raises:
                IndexError: If the list is empty
        '''
        ...

    @property
    @abstractmethod
    def empty(self) -> bool:

        ''' Returns True if the list is empty, False otherwise
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> linked_list.empty
                True
                >>> linked_list.append('dog')
                >>> linked_list.empty
                False
                
            Returns:
                True if the list is empty, False otherwise
        '''
        ...

    @abstractmethod
    def __len__(self) -> int:

        ''' Returns the number of items in the list
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> len(linked_list)
                0
                >>> linked_list.append('dog')
                >>> len(linked_list)
                1
                
            Returns:
                The number of items in the list
        '''
        ...

    @abstractmethod
    def __str__(self) -> str:
        
        ''' Returns a string representation of the list
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> str(linked_list)
                '()'
                >>> linked_list.append('dog')
                >>> str(linked_list)
                '(dog)'
                >>> linked_list.append('cat')
                >>> str(linked_list)
                '(dog <-> cat)'
                
            Returns:
                A string representation of the list
        '''
        ...

    @abstractmethod
    def __repr__(self) -> str:

        ''' Returns a string representation of the list
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> repr(linked_list)
                'LinkedList()'
                >>> linked_list.append('dog')
                >>> repr(linked_list)
                'LinkedList(dog) Count: 1'
                >>> linked_list.append('cat')
                >>> repr(linked_list)
                'LinkedList(dog <-> cat) Count: 2'
                

            Returns:
                A string representation of the list
        '''
        ...

    @abstractmethod
    def clear(self) -> None:

        ''' Removes all items from the list
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> linked_list.append('dog')
                >>> linked_list.append('cat')
                >>> linked_list.append('mouse')
                >>> linked_list.clear()
                >>> print(linked_list)
                ()
                
        '''
        ...

    @abstractmethod
    def __contains__(self, item: T) -> bool:

        ''' Returns True if the item is in the list, False otherwise
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> linked_list.append('dog')
                >>> linked_list.append('cat')
                >>> linked_list.append('mouse')
                >>> 'cat' in linked_list
                True
                >>> 'bird' in linked_list
                False
                

            Arguments:
                item: The item to check for in the list

            Returns:
                True if the item is in the list, False otherwise
        '''
        ...
    
    @abstractmethod
    def __iter__(self) -> ILinkedList[T]:

        ''' Returns an iterator for the list
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> linked_list.append('dog')
                >>> linked_list.append('cat')
                >>> linked_list.append('mouse')
                >>> for item in linked_list:
                ...     print(item)
                dog
                cat
                mouse
                

            Returns:
                An iterator for the list
        '''
        ...

    @abstractmethod
    def __next__(self) -> T:

        ''' Returns the next item in the list
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> linked_list.append('dog')
                >>> linked_list.append('cat')
                >>> linked_list.append('mouse')
                >>> iterator = iter(linked_list)
                >>> next(iterator)
                'dog'
                >>> next(iterator)
                'cat'
                >>> next(iterator)
                'mouse'
                >>> next(iterator)
                Traceback (most recent call last):
                    ...
                StopIteration
                

            Returns:
                The next item in the list

            Raises:
                StopIteration: If there are no more items in the list
        '''
        ...

    @abstractmethod
    def __eq__(self, other: object) -> bool:

        ''' Returns True if the list is equal to another list, False otherwise
        
            Examples:
                >>> linked_list1 = LinkedList(data_type=str)
                >>> linked_list1.append('dog')
                >>> linked_list1.append('cat')
                >>> linked_list1.append('mouse')
                >>> linked_list2 = LinkedList(data_type=str)
                >>> linked_list2.append('dog')
                >>> linked_list2.append('cat')
                >>> linked_list2.append('mouse')
                >>> linked_list1 == linked_list2
                True
                >>> linked_list2.append('bird')
                >>> linked_list1 == linked_list2
                False
                

            Arguments:
                other: The other list to compare to

            Returns:
                True if the list is equal to another list, False otherwise
        '''
        ...

    @abstractmethod
    def __reversed__(self) -> ILinkedList[T]:

        ''' Returns a reversed version of the list
        
            Examples:
                >>> linked_list = LinkedList(data_type=str)
                >>> linked_list.append('dog')
                >>> linked_list.append('cat')
                >>> linked_list.append('mouse')
                >>> reversed_list = reversed(linked_list)
                >>> print(reversed_list)
                (mouse <-> cat <-> dog)
                

            Returns:
                A reversed version of the list
        '''
        ...
        

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
