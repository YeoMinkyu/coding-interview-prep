def counting_sort(array: list[int], min_val: int, max_val: int) -> list[int]:
    """
    Sort the input array in ascending order using CountingSort.
    Time: O(n + k), where n is len(array), k is max_val - min_val + 1.
    Space: O(k).
    Example:
        Input: array = [3, 1, 4, 1], min_val = 1, max_val = 4 -> Output: [1, 1, 3, 4]
    Edge Cases:
        - Empty array: return []
        - Single element: return [array[0]]
        - Duplicates, negative numbers, large range
    Hint: Use a counting array to store frequencies, then reconstruct the sorted array.
    """

    if not array:
        return []
    
    k = max_val - min_val + 1
    shift = min_val
    count_array = [0] * k
    sorted_array = [None] * len(array)

    for key in array:
        count_array[key-shift] += 1
    
    for index in range(k-1):
        count_array[index+1] += count_array[index]
    
    for key in reversed(array):
        count_array[key-shift] -= 1
        sorted_array[count_array[key-shift]] = key

    return sorted_array
