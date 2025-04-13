class HashTable:

    _DELETED = object()

    def __init__(self, size):
        # Initialize a fixed-size array for the hash table
        # Set up storage for key-value pairs and handle empty slots
        self._table = [None] * size
        self._capacity = size
        self._size = 0

    def hash(self, k, m):
        """
        Compute the hash value for key k, where m is the size of the hash table

        Time Complexity: O(1)

        Args:
            k: key value
            m: size of the hash table

        Returns:
          int: an index in the range [0, m-1]
        """
        
        return k % m

    def add(self, key, value):
        """
        Add a key-value pair to the hash
        If key already exists, update its value
        Use linear probing to resolve

        Time Complexity: O(1), O(n) worst case(many collisions)

        Args:
            key: key value
            value: value to assign with key in the hash table

        Raises:
            ValueError : when the hash table is full
        """
        

        if self._size >= self._capacity:
            raise ValueError("Hash table is full")

        index = self.hash(key, self._capacity)
        initial_index = index

        while True:

            # Empty or deleted slot: insert new pair
            if self._table[index] is None or self._table[index] is self._DELETED:
                self._table[index] = (key, value)
                self._size += 1
                return
            # Key exists : update value
            elif self._table[index][0] == key:
                self._table[index] = (key, value)
                return
            
            # Collision: probe the next slot
            index = (index + 1) % self._capacity

            # Full cycle: table is full
            if initial_index == index:
                raise ValueError("Hash table is full")

    def exists(self, key):
        """
        Return True if the key exists in the hash table, False otherwise

        Time Complexity : O(1), O(n) worst case(many collisions)

        Args:
            key: key to check existence of same key in the hash table
        
        Returns:
            bool: True if same key already exists, otherwise False
        """
        
        index = self.hash(key, self._capacity)
        initial_index = index

        while True:
            if self._table[index] is None:
                return False
            elif self._table[index] is not self._DELETED and key == self._table[index][0]:
                return True
                
            index = (index + 1) % self._capacity
            
            if initial_index == index:
                return False

    def get(self, key):
        """
        Return the value associated with the key
        Handle case when key is not found

        Time Complexity : O(1), O(n) worst case(many collisions)

        Args:
            key: key to get value when the same key exists in the hash table
        
        Raises:
            KeyError: when key is not found
        
        Returns:
            int: value to be matched with key
        """
        
        index = self.hash(key, self._capacity)
        initial_index = index

        while True:
            if self._table[index] is None:
                raise KeyError(f"Key: {key} is not found")
            elif self._table[index] is not self._DELETED and key == self._table[index][0]:
                return self._table[index][1]

            index = (index + 1) % self._capacity

            if initial_index is index:
                raise KeyError(f"Key: {key} is not found")

    def remove(self, key):
        """
        Remove the key-value pair with the given key
        Handle case when key is not found

        Time Complexity : O(1), O(n) worst case(many collisions)

        Args:
            key: key to remove an elments in the hash table
        
        Raises:
            KeyError: when key is not found
        """
        
        index = self.hash(key, self._capacity)
        initial_index = index

        while True:
            if self._table[index] is None:
                raise KeyError(f"Key: {key} is not found")
            elif self._table[index] is not self._DELETED and key is self._table[index][0]:
                self._table[index] = self._DELETED
                self._size -= 1
                return
            
            index = (index + 1) % self._capacity

            if initial_index == index:
                raise KeyError(f"Key: {key} is not found")