class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

        You must not use any built-in exponent function or operator.

        For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

        Time Complexity: O(log n)

        [Link]: https://leetcode.com/problems/sqrtx/description/
        """
        left, right = 0, x

        while left <= right:
            
            mid = left + (right - left) // 2

            if x < (mid*mid):
                right = mid - 1
            elif x > (mid*mid):
                left = mid + 1
            else:
                return mid
        
        return left - 1