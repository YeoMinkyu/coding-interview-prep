class Vector:
    def __init__(self, initial_size=0):
        # Start with capacity 16 or next power of 2 if initial_size is larger
        # Simulate memory allocation for an int array

        self._capacity = 16 if initial_size <= 16 else 2 ** (initial_size - 1).bit_length()
        self._size = 0  # Number of items currently stored
        self._data = [0] * self._capacity  # "Raw" array, no fancy list methods

    @property
    def size(self) -> int:
        # Return number of items
        # Logic: Return self._size
        return self._size

    @property
    def capacity(self) -> int:
        # Return total capacity
        # Logic: Return self._capacity
        return self._capacity


    def at(self, index: int) -> int:
        # Return item at index (no [] indexing, simulate pointer jump)
        # Blow up if out of bounds
        """
        Time Complexity : O(1)
        """
        """
        Logic: 
        - Check if index < 0 or >= self._size, raise IndexError if true
        - "Pointer" jump: return self._data[index] (simulating *(data + index))
        """

        if index < 0 or index >= self.size:
            raise IndexError
        
        return self._data[index]


    def delete(self, index: int) -> None:
        # Delete item at index, shift elements left
        """
        Time Complexity : O(n) where n is size of array
        """
        """
        Logic:
        - Check bounds (index < 0 or >= self._size), raise IndexError if invalid
        - Shift: Loop from index+1 to self._size-1, move each item left
        - Decrement self._size
        """
        if index < 0 or index >= self.size or self.is_empty():
            raise IndexError
        
        for _idx in range(index + 1, self.size):
            self._data[_idx -1] = self._data[_idx]

        self._size -= 1
    

    def find(self, item: int) -> int:
        # Return first index of item, -1 if not found
        """
        Time Complexity : O(n) where n is size of array
        """
        """
        Logic:
        - Loop through 0 to self._size-1
        - If self._data[i] == item, return i
        - Return -1 if not found
        """
        
        for _idx in range(self.size):
            if self._data[_idx] == item:
                return _idx
        
        return -1
    

    def insert(self, index: int, item: int) -> None:
        # Insert item at index, shift elements right
        """
        Time Complexity : O(n) when n is self._size
        """
        """
         Logic:
        - Check bounds (index < 0 or > self._size), raise IndexError if invalid
        - If self._size == self._capacity, resize(self._capacity * 2)
        - Shift: Loop from self._size-1 down to index, move each item right
        - Set self._data[index] = item
        - Increment self._size
        """
        # Pseudo Logic:
        # if self.size + 1 >= self.capacity
        #    self._resize()
        # from index to self._size => re-location(from index +1 to self.size +1)
        # insert new item at index
        # self._size += 1

        if index < 0 or index > self.size:
            raise IndexError

        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        
        if not self.is_empty() :
            for _idx in range(self.size-1, index -1, -1):
                self._data[_idx + 1] = self._data[_idx]
        
        self._data[index] = item 
        self._size += 1
    

    def is_empty(self) -> bool:
        # Check if vector is empty
        """
        Time Complexity : O(1)
        """
        # Logic: Return True if self._size == 0, else False
        return self.size == 0

     
    def pop(self) -> int:
        # Remove and return last item, resize if size drops to 1/4 capacity
        """
        Time Complexity : O(1), O(n) when resizing
        """
        """
        Logic:
        - If is_empty(), raise IndexError
        - Get last item: item = self._data[self._size - 1]
        - Decrement self._size
        - If self._size > 0 and self._size == self._capacity // 4, resize(self._capacity // 2)
        - Return item
        """
        if self.is_empty():
            raise IndexError
        
        pop_result = self._data[self.size - 1]
        self._size -= 1

        if self.size <= (self.capacity // 4) and self.capacity > 16:
            self._resize(int(self.capacity // 2))
        
        return pop_result


    def prepend(self, item: int) -> None:
        # Insert at index 0
        """
        Time Complexity : O(n) where n is size of array
        """
        # Logic: Call insert(0, item)
        self.insert(0, item)


    def push(self, item: int) -> None:
        # Add item to end, resize if needed
        """
        Time Complexity : O(1), O(n) where resizing
        """
        """
        Logic:
        - If self._size == self._capacity, call resize(self._capacity * 2)
        - Set self._data[self._size] = item
        - Increment self._size
        """
        
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        
        self._data[self.size] = item
        self._size += 1
        

    def remove(self, item: int) -> None:
        # Remove all instances of item, shift elements left
        """
        Time Complexity : O(n²) in worst case where n is size of array
        """
        """
        Logic:
        - Loop through 0 to self._size-1
        - If self._data[i] == item, call delete(i) and adjust loop index
        """
        
        while True:
            idx = self.find(item)

            if idx == -1:
                break

            self.delete(idx)
        

    def _resize(self, new_capacity: int) -> None:
        # Private method to resize array
        """
        Time Complexity : O(n) where n is self._size
        """
        """
        Logic:
        - Create new array: new_data = [0] * new_capacity
        - Copy old data: Loop 0 to self._size, new_data[i] = self._data[i]
        - Update self._data = new_data
        - Update self._capacity = new_capacity
        """
        
        if new_capacity < 16:
            new_capacity = 16

        new_data = [0] * new_capacity

        for _idx in range(self.size):
            new_data[_idx] = self._data[_idx]

        self._data = new_data
        self._capacity = new_capacity