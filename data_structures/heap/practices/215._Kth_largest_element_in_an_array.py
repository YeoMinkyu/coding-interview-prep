from heapq import heapify, heappop
from typing import List
"""
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Time Complexity: O(n + klogn)
        """
        max_heap = [-num for num in nums]

        heapify(max_heap)

        for _ in range(k-1):
            heappop(max_heap)

        return -max_heap[0]
        