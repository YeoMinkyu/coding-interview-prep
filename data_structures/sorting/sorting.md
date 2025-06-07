
# Sorting

## Counting Sort

### Q&A

1. Why is a sorting better being stable?
2. How can I deal with minus value?
   - k = max_val - min_val + 1 // if value < 0 : index = min - item
3. How can I deal with the array of large range?

### Interview-Style Question / Follow-Up

**Question:**

Counting sort is very fast for certain situations, but not universally applicable.

1. Can you explain a scenario where you would not want to use counting sort, even if you know it’s fast?

   - Don’t use counting sort when:
     - The range is very large (e.g., sorting ages from 0 to 10^9 for only 1000 people: k = 1,000,000,000 would use huge memory!).
     - The data isn’t easily mapped to integers (like strings, floats with many decimals, or complex objects).
     - When the range of number is quite wide(?), I mean k(the range of the elements in the array) is much bigger than n(the size of an array)

2. How does counting sort compare to comparison-based sorts like merge sort or quicksort in terms of lower bounds and when to use them?

   - Lower bound: Comparison-based Sorting(MergeSort, HeapSort, etc.)
     - Has the lower bound as O(nlogn)
     - It’s been mathematically proven (using decision trees) that no comparison-based sorting algorithm can guarantee better than O(n log n) time in the worst case.
     - log₂(n!) ≈ n log n.
   - Lower bound: Counting Sort
     - It is not comparison-based Sorting
     - Counting sort runs in O(n + k) time, where:
       - n = number of elements
       - k = range of values (max_val - min_val + 1)
     - Counting sort uses indexing (array positions), not comparisons, so it isn’t limited by this bound.

   - When to use:
     - The range k of input values is not much bigger than n.
     - The values are all integers (or can be mapped to integers).