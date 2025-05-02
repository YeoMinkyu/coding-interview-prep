class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

        If target is not found in the array, return [-1, -1].

        Time Complexity: O(log n)

        [link]: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
        """

        if not nums:
            return [-1, -1]

        lower_boundary = self._search_lower_boundary(nums, target)
        upper_boundary = self._search_upper_boundary(nums, target)

        return [lower_boundary, upper_boundary]

    def _search_lower_boundary(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1

        lower_boundary = - 1

        while left <= right:

            mid = left + (right - left) // 2

            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                lower_boundary = mid
                right = mid - 1
            
        return lower_boundary
    
    def _search_upper_boundary(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1
        upper_boundary = -1

        while left <= right:

            mid = left + (right - left) // 2

            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                upper_boundary = mid
                left = mid + 1

        return upper_boundary