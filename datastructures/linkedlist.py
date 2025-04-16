from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Iterator, Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.__data_type = data_type
        self.__head: Optional[LinkedList.Node] = None
        self.__tail: Optional[LinkedList.Node] = None
        self.__count = 0

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        outputList = LinkedList(data_type=data_type)
        for item in sequence:
            outputList.append(item)
        
        return outputList

    def append(self, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError(f"{item} is not of type {self.__data_type}")
        new_node: LinkedList.Node = LinkedList.Node(data = item)

        if self.empty:
            self.__head = self.__tail = new_node
        else:
            self.__tail.next = new_node
            new_node.previous = self.__tail
            self.__tail = new_node
        
        self.__count += 1

    def prepend(self, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError(f"{item} is not of type {self.__data_type}")

        new_node: LinkedList.Node = LinkedList.Node(data = item)

        if self.empty:
            self.__head = self.__tail = new_node
        else:
            self.__head.previous = new_node
            new_node.next = self.__tail
            self.__head = new_node
        
        self.__count += 1

    def insert_before(self, target: T, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError(f"{item} is not of type {self.__data_type}")
        if not isinstance(target, self.__data_type):
            raise TypeError(f"{target} is not of type {self.__data_type}")
        target_node = LinkedList.__find_following(self.__head, target)
        if target_node is None:
            raise ValueError(f"The target item {target} is not in the linked list")
        new_node = LinkedList.Node(item)
        
        new_node.next = target_node
        new_node.previous = target_node.previous
        target_node.previous.next = new_node
        target_node.previous = new_node

        self.__count += 1

    def insert_after(self, target: T, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError(f"{item} is not of type {self.__data_type}")
        if not isinstance(target, self.__data_type):
            raise TypeError(f"{target} is not of type {self.__data_type}")
        target_node = LinkedList.__find_following(self.__head, target)
        if target_node is None:
            raise ValueError(f"The target item {target} is not in the linked list")
        new_node = LinkedList.Node(item)
        
        new_node.previous = target_node
        new_node.next = target_node.next
        target_node.next.previous = new_node
        target_node.next = new_node
        
        self.__count += 1

    def remove(self, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError(f"{item} is not of type {self.__data_type}")
        target_node = LinkedList.__find_following(self.__head, item)
        if target_node is None:
            raise ValueError(f"The target item {item} is not in the linked list")
        
        self.__remove_node(target_node)

    def remove_all(self, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError(f"{item} is not of type {self.__data_type}")
        target_node = LinkedList.__find_following(self.__head, item)
        while target_node is not None:
            self.__remove_node(target_node)

            target_node = LinkedList.__find_following(target_node.next, item)

    @staticmethod
    def __find_following(start: Node, target: T) -> Optional[Node]:
        """
        Internal helping function to find a node with target value
        O(n)
        Follow next from start until it finds target
        """
        travel = start

        while travel is not None:

            if travel.data == target:
                return travel

            travel = travel.next

        return None

    def __remove_node(self, target_node: Node):
        """
        internal helping function to remove a node from a reference
        O(1)
        """
        if target_node.next is None:
            self.__tail = target_node.previous
        else:
            target_node.next.previous = target_node.previous
        if target_node.previous is None:
            self.__head = target_node.next
        else:
            target_node.previous.next = target_node.next

        self.__count -= 1


    def pop(self) -> T:
        if self.__tail is None:
            raise IndexError("list is empty")
        
        out = self.__tail.data
        self.__remove_node(self.__tail)
        return out

    def pop_front(self) -> T:
        if self.__head is None:
            raise IndexError("list is empty")
        
        out = self.__head.data
        self.__remove_node(self.__head)
        return out

    @property
    def front(self) -> T:
        if self.__head is None:
            raise(IndexError("list is empty"))
        return self.__head.data

    @property
    def back(self) -> T:
        if self.__tail is None:
            raise(IndexError("list is empty"))
        return self.__tail.data

    @property
    def empty(self) -> bool:
        return len(self) == 0

    def __len__(self) -> int:
        return self.__count

    def clear(self) -> None:
        self.__head: Optional[LinkedList.Node] = None
        self.__tail: Optional[LinkedList.Node] = None
        self.__count = 0

    def __contains__(self, item: T) -> bool:
        return self.__find_following(self.__head, item) is not None

    def __iter__(self) -> ILinkedList[T]:
        self.__travel_node = self.__head
        return self

    def __next__(self) -> T:
        if self.__travel_node is None:
            raise StopIteration
        
        data = self.__travel_node.data
        self.__travel_node = self.__travel_node.next
        return data
    
    def __reversed__(self) -> Iterator[T]:
        #this is implemented as reccomended in class, but differs from the implementation described in ILinkedList
        #this also behaves slightly different from __iter__ in some unintuitive ways
        travel_node = self.__tail

        while travel_node is not None:
            yield travel_node.data

            travel_node = travel_node.previous
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False
        if len(self) != len(other):
            return False
        for node1, node2 in zip(self, other):
            if node1 != node2:
                return False
        return True

    def __str__(self) -> str:
        items = []
        current = self.__head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.__head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.__count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
