class Queue:
    def __init__(self, capacity):
        # Initialize a fixed-sized array queue with a given capacity
        # Set up array and pointers (e.g., front, rear) to track queue state
        self._queue = [None] * capacity
        self._capacity = capacity
        self._size = 0
        self._front = 0
        self._rear = 0

    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self._size

    @property
    def front(self):
        return self._front
    
    @property
    def rear(self):
        return self._rear

    def enqueue(self, value: int):
        """
        Add a value to the end of the available storage
        Handle case when queue is full"

        Args:
            int : the value to enqueue

        Raise:
            ValueError: When the queie is full

        Time Complexity: O(1)
        Space Complexity: O(1)
        """

        if self.full():
            raise ValueError("queue is full.")
        
        self._queue[self.rear] = value
        self._size += 1
        self._rear = (self.rear + 1) % self.capacity

    def dequeue(self):
        """
        Remove and return the value at the front of the queue
        Handle case when queue is empty

        Returns:
            int : The value to dequeue

        Raise:
            ValueError: When the queue is empty

        Time Complexity: O(1)
        Space Complexity: O(1) 
        """
        
        if self.empty():
            raise ValueError("queue is empty.")
        
        value = self._queue[self.front]
        self._size -= 1
        self._front = (self.front + 1) % self.capacity

        return value

    def empty(self):
        """
        Return True if the queue is empty, False otherwise

        Returns:
            bool: True if the queue is empty, False otherwise

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        
        return self.size == 0

    def full(self):
        """
        Return True if the queue is full, False otherwise

        Returns:
            bool: True if the queue is full, False otherwise
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        
        return self.size == self.capacity
