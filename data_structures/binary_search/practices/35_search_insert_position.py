class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

        Time Complexity : O(log n)

        [link] https://leetcode.com/problems/search-insert-position/description/
        """
        
        if not nums:
            return -1
        
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right-left) // 2

            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid

        return left 