class Node:
    def __init__(self, value: int):
        # Initialize a node with a value and a next pointer
        self._value = value
        self._next = None

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value: int):
        self._value = value

    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, node):
        self._next = node


class Queue:
    def __init__(self):
        # Initialize an empty queue with head and tail pointers
        self._head = None
        self._tail = None

    @property
    def head(self):
        return self._head
    
    @property
    def tail(self):
        return self._tail

    def enqueue(self, value: int):
        """
        Add a value to the tail of the queue

        Args:
            value(int) : The value to enqueue

        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        new_node = Node(value)

        if self.empty():
            self._head = new_node
            self._tail = new_node
        else:
            self.tail.next = new_node
            self._tail = new_node

    def dequeue(self):
        """
        Remove and return the value at the front of the queue
        Raise an exception if the queue is empty

        Returns:
            int: The value at the front of the queue

        Raise:
            ValueError: If the queue is empty 

        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        if self.empty():
            raise ValueError("Queue is empty.")

        value = self.head.value
        if self.head is self.tail:
            self._head = None
            self._tail = None
        else:
            self._head = self.head.next

        return value

    def empty(self):
        """
        Return True if the queue is empty, otherwise return False

        Returns:
            bool: Whether the queue is empty

        Time Complexity : O(1)
        Space Complexity : O(1)
        """
        return self.head is None
    
    def __str__(self):
        """
        Return a string representation of the queue

        Returns:
            str: A string to show the queue's elements
        """
        if self.empty():
            return "Queue: []"
        
        values = []

        current_node = self.head

        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next
        
        return "Queue" + " -> ".join(values) + " -> None"