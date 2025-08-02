import random

def quick_sort(array: list[int], low: int, high: int) -> None:
    
    if low >= high:
        return

    pivot_index = partition(array, low, high)

    quick_sort(array, low, pivot_index-1)
    quick_sort(array, pivot_index +1, high)


def partition(array: list[int], low: int, high: int) -> int:
    
    mid = (low+high) // 2

    if array[low] < array[mid]:
        if array[high] > array[mid]:
            median_index = mid
        elif array[low] < array[high]:
            median_index = high
        else:
            median_index = low
    else: # array[low] > array[mid]
        if array[low] > array[high]:
            median_index = high
        elif array[high] > array[mid]:
            median_index = high
        else:
            median_index = mid
        
    array[median_index], array[high] = array[high], array[median_index]

    i = low - 1
    j = low

    while j < high:
        if array[j] <= array[high]:
            i += 1
            array[i], array[j] = array[j], array[i]

        j += 1

    pivot_index = i+1
    array[pivot_index], array[high] = array[high], array[pivot_index]

    return pivot_index


     































# def quick_sort(array: list[int], low: int, high: int) -> None:
#     """
#     Sort the input array in-place in ascending order using QuickSort.
#     Time: O(n log n) average, O(n^2) worst case, Space: O(log n) average.
#     Example:
#         Input: array = [3, 1, 4, 2], low = 0, high = 3 -> Output: [1, 2, 3, 4]
#     Edge Cases:
#         - Empty array or invalid range: no-op
#         - Single element: already sorted
#         - Duplicates, negative numbers, already sorted arrays
#     Hint: Choose a pivot, partition the array, and recurse on subarrays.
#     """
#     if low >= high:
#         return
    
#     pivot_index = _partition(array, low, high)
#     quick_sort(array, low, pivot_index - 1)
#     quick_sort(array, pivot_index + 1, high)

# def _partition(array: list[int], low: int, high: int) -> int:
#     """
#     Partition the array around a pivot and return the pivot's final index.
#     Lumoto Partitioning.
#     In Python, built-in sort() uses Timsort, a hybrid of merge sort and insertion sort.

#     Time: O(n), Space: O(1).
#     Example:
#         Input: array = [3, 1, 4, 2], low = 0, high = 3 -> Output: 2 (pivot 2 at index 2)
#     Edge Cases:
#         - All elements equal
#         - Pivot is smallest or largest
#     Hint: Choose pivot (e.g., last element), place it in correct position.
#     """
   

#     pivot_index = random.randrange(low, high+1)
#     array[high], array[pivot_index] = array[pivot_index], array[high]

#     larger_index = low - 1

#     for smaller_index in range(low, high):
#         if array[smaller_index] <= array[high]:
#             larger_index += 1
#             array[smaller_index], array[larger_index] = array[larger_index], array[smaller_index]

#     array[high], array[larger_index+1] = array[larger_index+1], array[high]

#     return larger_index + 1