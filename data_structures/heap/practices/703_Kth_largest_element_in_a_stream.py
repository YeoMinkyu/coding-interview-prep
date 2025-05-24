"""
Time limit exceeded approach
(using min & max heap)

First Attempt

    - My first idea was using max heap(or min heap) after implementing the codes and sorting using heap sort and then return Kth largest element in the stream.

    But it eventually revealed time limit exceeded when I submit the code.

Time Complexity:
    Build(heapify) : O(n)
    Insert : O(logn)
    Extract : O(logn)
    Heapsort : O(nlogn)

What I learned?

    - I learned how to use libaray of `heapq` in Python.
    - I don't need to keep whole array(or List), I just need to keep partial array(size of k) for tracking Kth largest element 

"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = []
        self.k = k

        for num in nums:
            self.insert_val(num)
            if len(self.stream) > self.k:
                self.extract_min()

    def add(self, val: int) -> int:
        self.insert_val(val)
        
        if len(self.stream) > self.k:
            self.extract_min()
        
        return self.stream[0]

    def insert_val(self, val: int) -> None:
        self.stream.append(val)
        self.sift_up(len(self.stream)-1)

    def extract_min(self) -> None:
        self.stream[0], self.stream[-1] = self.stream[-1], self.stream[0]
        self.stream.pop()
        self.sift_down(0)
         
    def sift_up(self, index: int) -> None:

        while True:
            parent = (index - 1) // 2

            if self.stream[parent] > self.stream[index] and parent >= 0:
                self.stream[parent], self.stream[index] = self.stream[index], self.stream[parent]
                index = parent
            else:
                break



    def sift_down(self, index: int) -> None:
        smallest = index

        while True:
            left_child_index = (2 * index) + 1
            right_child_index = (2 * index) + 2

            if left_child_index < len(self.stream) and self.stream[left_child_index] < self.stream[smallest]:
                smallest = left_child_index
            if right_child_index < len(self.stream) and self.stream[right_child_index] < self.stream[smallest]:
                smallest = right_child_index
            if smallest == index:
                break

            self.stream[smallest], self.stream[index] = self.stream[index], self.stream[smallest]
            index = smallest


# Time limit exceeded (using min heap)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        self.k = k

    def add(self, val: int) -> int:
        self.heapify(self.stream)
        self.stream.append(val)
        self.sift_up(len(self.stream) - 1)

        updated_len = len(self.stream)
        for _ in range(len(self.stream) - self.k):
            self.extract_root(updated_len)
            updated_len -= 1
            self._sift_down(0, updated_len)
        
        return self.stream[0]
    
    def extract_root(self, updated_len: int) -> None:
        self.stream[0], self.stream[updated_len - 1] = self.stream[updated_len - 1], self.stream[0]
    
    def _sift_down(self, index: int, updated_len: int) -> None:

        while True:
            smallest = index
            left_child_index = (2*index) + 1
            right_child_index = (2*index) + 2

            if left_child_index < updated_len and self.stream[smallest] > self.stream[left_child_index]:
                smallest = left_child_index
            if right_child_index < updated_len and self.stream[smallest] > self.stream[right_child_index]:
                smallest = right_child_index
            if smallest == index:
                break
            
            self.stream[index], self.stream[smallest] = self.stream[smallest], self.stream[index]
            index = smallest
        
    def heapify(self, array: List[int]) -> None:
        if not self.stream:
            return

        current_index = (len(self.stream) - 1 - 1) // 2

        while current_index >= 0:
            self.sift_down(current_index)
            current_index -= 1

    def sift_down(self, index: int) -> None:
    
        while True:
            smallest = index
            left_child_index = (2*index) + 1
            right_child_index = (2*index) + 2

            if left_child_index < len(self.stream) and self.stream[smallest] > self.stream[left_child_index]:
                smallest = left_child_index
            if right_child_index < len(self.stream) and self.stream[smallest] > self.stream[right_child_index]:
                smallest = right_child_index
            if smallest == index:
                break

            self.stream[index], self.stream[smallest] = self.stream[smallest], self.stream[index]
            index = smallest

    def sift_up(self, index: int) -> None:
        current_index = index
        while current_index > 0:
            parent = (current_index - 1) // 2

            if self.stream[parent] > self.stream[current_index]:
                self.stream[parent], self.stream[current_index] = self.stream[current_index], self.stream[parent]
                current_index = parent
            else:
                break

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Time limit exceeded (sovling with max heap)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums
        self.heapify(self.stream)
        

    def add(self, val: int) -> int:
        self.insert_value(val)
        self.heapsort(self.stream)
        
        return self.stream[-self.k]

    def heapify(self, array: List[int]) -> None:
        if not self.stream:
            return

        current_index = (len(self.stream) - 1 - 1) // 2

        while current_index >= 0:
            self.sift_down(current_index)
            current_index -= 1

    def heapsort(self, array: List[int]) -> None:
        self.heapify(self.stream)

        heap_len = len(self.stream)

        while heap_len > 1:
            self.stream[0], self.stream[heap_len - 1] = self.stream[heap_len - 1], self.stream[0]
            heap_len -= 1
            self._sift_down(0, heap_len)
    
    def _sift_down(self, index: int, len: int) -> None:

        while True:
            largest = index
            left_child_index = (2*index) + 1
            right_child_index = (2*index) + 2

            if left_child_index < len and self.stream[largest] < self.stream[left_child_index]:
                largest = left_child_index
            if right_child_index < len and self.stream[largest] < self.stream[right_child_index]:
                largest = right_child_index
            if largest == index:
                break
            
            self.stream[index], self.stream[largest] = self.stream[largest], self.stream[index]
            index = largest
        
    def insert_value(self, val: int) -> None:
        self.stream.append(val)
        self.sift_up(len(self.stream) - 1)

    def sift_up(self, index: int) -> None:
        current_index = index
        while current_index >= 0:
            parent = (current_index - 1) // 2

            if self.stream[parent] < self.stream[current_index]:
                self.stream[parent], self.stream[current_index] = self.stream[current_index], self.stream[parent]
                current_index = parent
            else:
                break


    def sift_down(self, index: int) -> None:
    
        while True:
            largest = index
            left_child_index = (2*index) + 1
            right_child_index = (2*index) + 2

            if left_child_index < len(self.stream) and self.stream[largest] < self.stream[left_child_index]:
                largest = left_child_index
            if right_child_index < len(self.stream) and self.stream[largest] < self.stream[right_child_index]:
                largest = right_child_index
            if largest == index:
                break

            self.stream[index], self.stream[largest] = self.stream[largest], self.stream[index]
            index = largest
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)