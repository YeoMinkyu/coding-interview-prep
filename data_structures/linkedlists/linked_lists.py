class Node:
    def __init__(self, num: int):
        # Initialize a node with a value and a next pointer
        self._value = num
        self._next = None

    @property
    def value(self) -> int:
        return self._value
    
    @value.setter
    def value(self, num: int):
        self._value = num

    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, node):
        self._next = node


class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with a head pointer
        self._head = None

    @property
    def head(self):
        return self._head
    
    @property
    def size(self):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Return the number of data elements in the list
        size = 0
        count_head = self.head

        if self.head is None:
            return size
        
        while count_head:
            size += 1
            count_head = count_head.next
        
        return size

    @property
    def empty(self):
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Return True if the list is empty, False otherwise

        return self.head is None

    def value_at(self, index):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Return the value of the node at the given index (0-based)
        # Raise an exception if index is invalid
        
        if index < 0 or index >= self.size:
            raise IndexError
        
        current_node = self.head

        for _ in range(index):
            current_node = current_node.next
        
        return current_node.value


    def push_front(self, value):
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Add a new node with the given value to the front of the list
        
        new_node = Node(value)

        if self.empty:
            self._head = new_node
        else:
            new_node.next = self._head
            self._head = new_node

    def pop_front(self):
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Remove the front node and return its value
        # Raise an exception if the list is empty
        if self.empty:
            raise ValueError
        
        value = self.head.value
        self._head = self.head.next

        return value

    def push_back(self, value):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Add a new node with the given value to the end of the list
        new_node = Node(value)
        current_node = self.head

        if self.empty:
            self._head = new_node
        else:
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def pop_back(self):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Remove the last node and return its value
        # Raise an exception if the list is empty
        if self.empty:
            raise ValueError
        
        current_node = self.head
        current_size = self.size
        
        if current_size == 1:
            self._head = None
            return current_node.value
        else: 
            while current_node.next.next:

                current_node = current_node.next

            value = current_node.next.value

            current_node.next = None

            return value

    def front(self):
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Return the value of the front node
        # Raise an exception if the list is empty
        if self.empty:
            raise ValueError
        
        return self.head.value

    def back(self):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Return the value of the last node
        # Raise an exception if the list is empty
        if self.empty:
            raise ValueError

        current_node = self.head
        
        while current_node.next:
            current_node = current_node.next
        
        return current_node.value

    def insert(self, index, value):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Insert a new node with the given value at the specified index
        # The current node at that index becomes the next node of the new node
        # Raise an exception if index is invalid
        if index < 0 or index > self.size:
            raise IndexError
        
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self._head = new_node
        else:
            current_node = self.head
            for _ in range(index-1):
                current_node = current_node.next
            
            new_node.next = current_node.next
            current_node.next = new_node
        

    def erase(self, index):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Remove the node at the given index
        # Raise an exception if index is invalid or list is empty
        if index < 0 or index >= self.size:
            raise IndexError

        current_node = self.head

        if index == 0:
            self._head = current_node.next
        else:
            for _ in range(index):
                previous_node = current_node
                current_node = current_node.next

            previous_node.next = current_node.next

    def value_n_from_end(self, n):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Return the value of the node at the nth position from the end
        # Raise an exception if n is invalid or list is too short
        
        if n < 0 or n >= self.size or self.empty:
            raise IndexError
        
        index = self.size - (n+1)

        return self.value_at(index)

    def reverse(self):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Reverse the entire linked list in place
        if self.empty:
            raise ValueError
        if self.size <= 1:
            return
        
        # TBD : REVIEW!
        previous_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self._head = previous_node

    def remove_value(self, value):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Remove the first node with the given value
        # Do nothing if value is not found
        if self.empty:
            raise ValueError

        if self.head.value == value:
            self._head = self.head.next
            return
       
        current_node = self.head

        # TBD : REVIEW!
        while current_node.next:
            if value == current_node.next.value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def __str__(self):
        """Return a string representation of the linked list."""
        if self.empty:
            return "[]"
        values = []
        current = self.__head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) + " -> None"