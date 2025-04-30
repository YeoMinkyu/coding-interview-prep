class BinarySearch:
    def binary_search(self, arr, target):
        """
        Perform iterative binary search to find the target in the sorted array
        Args:
            arr(list): A sorted list of integers in ascending order.
            target(int): The value to search for.
        Returns:
            int: The index of the target if found, otherwise return -1

        Time Complexity: O(log n), Halves the search interval each iteration
        Space Complexity: O(1)
        """
        if not arr: # Handle emptry or None array
            return -1

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if target < arr[mid]:
                right = mid -1
            elif target > arr[mid]:
                left = mid + 1
            else:
                return mid
        
        return -1

    def binary_search_recursive(self, arr, target):
        """
        Perform recursive binary search to find the target in the sorted array
        
        Args:
            arr(list): A sorted list of integers in ascending order.
            target(int): The value to search for.
        
        Returns:
            int: The index of the target if found, otherwise return -1

        Time Complexity: O(log n), Halves the search interval each iteration
        Space Complexity: O(1)
        """
        

        if not arr:
            return -1

        return self._binary_search_helper(arr, 0, len(arr) - 1, target)

    def _binary_search_helper(self, arr, left, right, target):
        """
        Helper funtion for reculsive binary search

        Args:
            arr(list): A sorted list of integers in ascending order.
            left(int): The left boundary of the search interval.
            right(int): The right boundary of the search interval.
            targer(int): The value to search for.

        Returns:
            int : The index of the target if found, otherwise return -1
        """

        if left > right:
            return -1
        
        mid = left + (right - left) // 2

        if target < arr[mid]:
            return self._binary_search_helper(arr, left, mid-1, target)
        elif target > arr[mid]:
            return self._binary_search_helper(arr, mid+1, right, target)
        else:
            return mid
        