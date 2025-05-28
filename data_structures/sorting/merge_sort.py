def merge_sort(array: list[int]) -> list[int]:
    """
    Sort the input array in ascending order using MergeSort.
    Time: O(n log n), Space: O(n).
    Example:
        Input: array = [3, 1, 4, 2] -> Output: [1, 2, 3, 4]
        Input: array = [5, 5, 5] -> Output: [5, 5, 5]
    Edge Cases:
        - Empty array: return []
        - Single element: return [array[0]]
        - Duplicates, negative numbers, large arrays
    Hint: Divide array into halves, recursively sort, and merge sorted halves.
    """
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left_sorted = merge_sort(array[:mid])
    right_sorted = merge_sort(array[mid:])

    return _merge(left_sorted, right_sorted)

def _merge(left: list[int], right: list[int]) -> list[int]:
    """
    Merge two sorted arrays into a single sorted array.
    Time: O(n), Space: O(n), where n is len(left) + len(right).
    Example:
        Input: left = [1, 3], right = [2, 4] -> Output: [1, 2, 3, 4]
    Edge Cases:
        - One or both arrays empty
        - Arrays with duplicates
    Hint: Compare elements and build a merged result array.
    """
    sorted_array = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right): 
        if left[left_index] <= right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
        
    if left_index < len(left):
        sorted_array.extend(left[left_index:])
    elif right_index < len(right):
        sorted_array.extend(right[right_index:])

    return sorted_array

