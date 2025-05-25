"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Time Complexity : O(klogn)

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

[Link] : https://leetcode.com/problems/top-k-frequent-elements/?envType=problem-list-v2&envId=heap-priority-queue
"""

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        self.frequency = dict()
        self.min_heap = []

        for num in nums:
            self.frequency[num] = self.frequency.get(num, 0) + 1
        
        self.add(k)

        return [num for _, num in self.min_heap]

    def add(self, k: int) -> None:
        for num, frequency in self.frequency.items():
            heapq.heappush(self.min_heap, (frequency, num))
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)

"""
Implemented data structure of min-heap on my own. 
"""               
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        self.frequency = dict()
        self.min_heap = []

        for num in nums:
            self.frequency[num] = 0

        for num in nums:
            self.frequency[num] += 1

        self.add(k)

        return [num for num, _ in self.min_heap]

    def add(self, k: int) -> None:
        for num, frequency in self.frequency.items():
            self.min_heap.append((num, frequency))
            self.sift_up(len(self.min_heap) - 1)
            if len(self.min_heap) > k:
                self.extract_min()

    def sift_up(self, index: int) -> None:
        while True:
            parent = (index - 1) // 2
            if self.min_heap[parent][1] > self.min_heap[index][1] and parent >= 0:
                self.min_heap[parent], self.min_heap[index] = self.min_heap[index], self.min_heap[parent]
                index = parent
            else:
                break

    def extract_min(self) -> None:
        self.min_heap[0], self.min_heap[-1] = self.min_heap[-1], self.min_heap[0]
        self.min_heap.pop()
        self.sift_down(0)

    def sift_down(self, index: int) -> None:
        smallest = index

        while True:
            left_child_index = (2 * index) + 1
            right_child_index = (2 * index) + 2

            if left_child_index < len(self.min_heap) and self.min_heap[left_child_index][1] < self.min_heap[smallest][1]:
                smallest = left_child_index
            if right_child_index < len(self.min_heap) and self.min_heap[right_child_index][1] < self.min_heap[smallest][1]:
                smallest = right_child_index
            if index == smallest:
                break

            self.min_heap[smallest], self.min_heap[index] = self.min_heap[index], self.min_heap[smallest]

            index = smallest