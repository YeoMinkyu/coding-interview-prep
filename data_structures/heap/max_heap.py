class MaxHeap:
    def __init__(self):
        """Initialize an empty max-heap."""
        self.heap = []

    def insert(self, value: int) -> None:
        """
        Insert a value into the max-heap, maintaining the heap property.
        Time: O(log n), where n is the number of elements.
        Example:
            Input: value = 5, heap = [] -> Heap: [5]
            Input: value = 3, heap = [5] -> Heap: [5, 3]
        Edge Cases:
            - Empty heap (insert as root).
            - Multiple insertions maintaining max-heap property.
        Hint: Append value to the end and sift up.
        """

        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)
    

    def sift_up(self, index: int) -> None:
        """
        Sift up the element at the given index to restore the max-heap property.
        Time: O(log n).
        Example:
            Input: index = 1, heap = [5, 10, 3] -> Heap: [10, 5, 3]
        Edge Cases:
            - Sifting from root (no-op).
            - Single element.
        Hint: Compare with parent and swap if larger.
        """
        if index == 0:
            return
        
        parent_index = (index - 1) // 2

        if self.heap[parent_index] < self.heap[index]:
            # Swap value using tuple
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self.sift_up(parent_index)
        else:
            return 

    def get_max(self) -> int:
        """
        Return the maximum value in the heap without removing it.
        Time: O(1).
        Example:
            Input: heap = [5, 3, 2] -> Output: 5
        Edge Cases:
            - Empty heap (raise ValueError).
        """

        if self.is_empty():
            raise ValueError("Empty heap")
        
        return self.heap[0]

    def get_size(self) -> int:
        """
        Return the number of elements in the heap.
        Time: O(1).
        Example:
            Input: heap = [5, 3, 2] -> Output: 3
            Input: heap = [] -> Output: 0
        Edge Cases:
            - Empty heap.
        """
        return len(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if the heap is empty, False otherwise.
        Time: O(1).
        Example:
            Input: heap = [] -> Output: True
            Input: heap = [5] -> Output: False
        """
        if self.heap:
            return False
        else:
            return True

    def extract_max(self) -> int:
        """
        Remove and return the maximum value from the heap, maintaining the heap property.
        Time: O(log n).
        Example:
            Input: heap = [5, 3, 2] -> Output: 5, Heap: [3, 2]
        Edge Cases:
            - Empty heap (raise ValueError).
            - Single element.
        Hint: Swap root with last element, remove last, and sift down.
        """
        if self.is_empty():
            raise ValueError("Empty heap")
        
        if self.get_size() == 1:
            return self.heap.pop()
        else:
            max_value = self.heap[0]
            self.heap[0] = self.heap[len(self.heap) - 1]
            self.heap.pop()
            self.sift_down(0)
            return max_value

    def sift_down(self, index: int) -> None:
        """
        Sift down the element at the given index to restore the max-heap property.
        Time: O(log n).
        Example:
            Input: index = 0, heap = [1, 5, 3] -> Heap: [5, 1, 3]
        Edge Cases:
            - Sifting from leaf (no-op).
            - Single element.
        Hint: Compare with largest child and swap if smaller.
        """
        if self.is_empty():
            return
    
        parent = index
        left_child_index = (2 * index) + 1
        right_child_index = (2 * index) + 2


        # TODO: Imporve my code as simple version / Iterative version
        if left_child_index > (len(self.heap) - 1): # leaf node
            return
        elif right_child_index > (len(self.heap) - 1): # left child only
            if self.heap[parent] < self.heap[left_child_index]:
                self.heap[parent], self.heap[left_child_index] = self.heap[left_child_index], self.heap[parent] 
                self.sift_down(left_child_index)
            else:
                return
        else:
            if self.heap[left_child_index] >= self.heap[right_child_index]:
                if self.heap[parent] < self.heap[left_child_index]:
                    self.heap[parent], self.heap[left_child_index] = self.heap[left_child_index], self.heap[parent]
                    self.sift_down(left_child_index)
            else:
                if self.heap[parent] < self.heap[right_child_index]:
                    self.heap[parent], self.heap[right_child_index] = self.heap[right_child_index], self.heap[parent]
                    self.sift_down(right_child_index)

    def swap_value(self, first_index: int, second_index: int) -> None:
        temp_value = self.heap[first_index]
        self.heap[first_index] = self.heap[second_index]
        self.heap[second_index] = temp_value

    def remove(self, index: int) -> None:
        """
        Remove the element at the given index, maintaining the heap property.
        Time: O(log n).
        Example:
            Input: index = 1, heap = [5, 3, 2] -> Heap: [5, 2]
        Edge Cases:
            - Invalid index (raise ValueError).
            - Removing last element.
            - Removing root.
        Hint: Replace with last element, remove last, and sift up/down as needed.
        """
        if index < 0 or index > (len(self.heap) - 1):
            raise ValueError("Index is invalid")
        if index == (len(self.heap) - 1): # Remove last element
            self.heap.pop()
            return
        # if index == 0:
        #     self.heap[0] = self.heap.pop()
        #     self.sift_down(0)

        self.heap[index] = self.heap.pop()
        
        if index > 0 and self.heap[(index - 1) // 2] < self.heap[index]:
            self.sift_up(index)
        else:
            self.sift_down(index)

    def heapify(self, array: list[int]) -> None:
        """
        Convert an array into a max-heap in-place.
        Time: O(n).
        Example:
            Input: array = [3, 1, 4] -> Heap: [4, 1, 3]
        Edge Cases:
            - Empty array.
            - Single element.
        Hint: Start from last non-leaf node and sift down each node.
        """
        self.heap = array

        if self.is_empty():
            return
        
        current_index = (len(self.heap) - 1)

        # TODO : How can I calcuate index of last non-leaf node.
        while current_index >= 0:
            self.sift_down(current_index)
            current_index -= 1
            

    def heap_sort(self, array: list[int]) -> None:
        """
        Sort the input array in-place in ascending order using a max-heap.
        Time: O(n log n).
        Example:
            Input: array = [3, 1, 4, 2] -> Array: [1, 2, 3, 4]
        Edge Cases:
            - Empty array.
            - Single element.
            - Array with duplicates.
        Hint: Heapify array, then repeatedly extract max and place at end.
        """

        self.heapify(array)
        
        heap_len = len(self.heap)

        while heap_len > 1:
            self.heap[0], self.heap[heap_len-1] = self.heap[heap_len-1], self.heap[0]
            heap_len -= 1
            self._sift_down_for_heap_sort(0, heap_len)


    def _sift_down_for_heap_sort(self, index: int, heap_len: int) -> None:
        parent = index
        left_child_index = (2 * index) + 1
        right_child_index = (2 * index) + 2

        if left_child_index > (heap_len - 1): # leaf node
            return
        elif right_child_index > (heap_len - 1): # left child only
            if self.heap[parent] < self.heap[left_child_index]:
                self.heap[parent], self.heap[left_child_index] = self.heap[left_child_index], self.heap[parent]
                self._sift_down_for_heap_sort(left_child_index, heap_len)
            else:
                return
        else:
            if self.heap[left_child_index] >= self.heap[right_child_index]:
                if self.heap[parent] < self.heap[left_child_index]:
                    self.heap[parent], self.heap[left_child_index] = self.heap[left_child_index], self.heap[parent]
                    self._sift_down_for_heap_sort(left_child_index, heap_len)
            else:
                if  self.heap[parent] < self.heap[right_child_index]:
                    self.heap[parent], self.heap[right_child_index] = self.heap[right_child_index], self.heap[parent]
                    self._sift_down_for_heap_sort(right_child_index, heap_len)
