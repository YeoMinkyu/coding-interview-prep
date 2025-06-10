def radix_sort(array: list[int]) -> list[int]:
    """
    Sort the input array in ascending order using RadixSort (LSD).
    Time: O(d(n + k)), where n is len(array), d is max digits, k is base (10).
    Space: O(n + k).
    Example:
        Input: array = [170, 45, 75, 90] -> Output: [45, 75, 90, 170]
    Edge Cases:
        - Empty array: return []
        - Single element: return [array[0]]
        - Duplicates, negative numbers, large numbers
    Hint: Process digits from least to most significant using CountingSort.
    """

    if not array:
        return []

    sorted_array = []
    negative_array = []
    positive_array = []

    for num in array:
        if num < 0:
            negative_array.append(abs(num))
        else:
            positive_array.append(num)

    largest = max(positive_array)
    d = len(str(largest))

    for exp in range(d):
        positive_array = _counting_sort_for_digit(positive_array, exp)

    if len(negative_array) > 0:
        largest = max(negative_array)
        d = len(str(largest))

        for exp in range(d):
            negative_array = _counting_sort_for_digit(negative_array, exp)
        
        for num in reversed(negative_array):
            sorted_array.append(-num)
    
    sorted_array.extend(positive_array)

    return sorted_array

def _counting_sort_for_digit(array: list[int], exp: int) -> list[int]:
    """
    Sort the array based on the digit represented by exp (10^exp) using CountingSort.
    Time: O(n + k), where n is len(array), k is base (10).
    Space: O(n + k).
    Example:
        Input: array = [170, 45, 75, 90], exp = 1 -> Output: [170, 90, 45, 75]
    Edge Cases:
        - Digits beyond max length
        - Negative numbers
    Hint: Use CountingSort to sort based on the current digit.
    """
    
    k = 10
    counting_buckets = [[] for _ in range(k)] 
    sorted_array = []
    divisor = k ** exp

    for num in array:
        count_index = int((num // divisor) % k)
        counting_buckets[count_index].append(num)

    for sub_array in counting_buckets:
        if sub_array:
            sorted_array.extend(sub_array)

    return sorted_array

