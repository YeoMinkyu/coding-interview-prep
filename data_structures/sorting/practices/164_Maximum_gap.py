from typing import List

"""
164. Maximum Gap

Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

 

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
"""

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        largetst = max(nums)
        digit = len(str(largetst))

        sorted_array = nums

        for exp in range(digit):
            sorted_array = self._counting_sort(sorted_array, exp)

        max_gap = 0

        for i in range(len(sorted_array)-1):
            max_gap = max(max_gap, sorted_array[i+1] - sorted_array[i])

        return max_gap

    def _counting_sort(self, array: List[int], exp: int) -> List[int]:
        k = 10
        divisor = k ** exp

        counting_sort_array = [[] for _ in range(k)]
        sorted_array = []

        for num in array:
            count = (num // divisor) % k
            counting_sort_array[count].append(num)

        for sub_array in counting_sort_array:
            sorted_array.extend(sub_array)
        
        return sorted_array
