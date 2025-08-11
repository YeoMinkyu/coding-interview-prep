"""
373. Find K Pairs with Smallest Sums

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

"""

from heapq import heappush, heappop
from typing import *

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        Time Complexity: O(klogk)
        Space Complexity: O(k)
        """
        answer = []
        min_heap = []

        for i in range(min(k, len(nums1))):
            heappush(min_heap, (nums1[i]+nums2[0], i, 0))
        
        while len(answer) < k:
            sum, i, j = heappop(min_heap)
            answer.append([nums1[i], nums2[j]])

            if j+1 < len(nums2):
                heappush(min_heap, (nums1[i]+nums2[j+1], i, j+1))

        return answer
