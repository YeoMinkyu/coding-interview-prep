import unittest
from data_structures.sorting.merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_basic_sorting(self):
        """Test sorting a standard array."""
        arr = [3, 1, 4, 2]
        self.assertEqual(merge_sort(arr), [1, 2, 3, 4])

    def test_empty_array(self):
        """Test sorting an empty array."""
        arr = []
        self.assertEqual(merge_sort(arr), [])

    def test_single_element(self):
        """Test sorting a single-element array."""
        arr = [5]
        self.assertEqual(merge_sort(arr), [5])

    def test_duplicates(self):
        """Test sorting an array with duplicates."""
        arr = [5, 2, 5, 1, 2]
        self.assertEqual(merge_sort(arr), [1, 2, 2, 5, 5])

    def test_negative_numbers(self):
        """Test sorting an array with negative numbers."""
        arr = [-3, 1, -5, 2, -1]
        self.assertEqual(merge_sort(arr), [-5, -3, -1, 1, 2])

    def test_already_sorted(self):
        """Test sorting an already sorted array."""
        arr = [1, 2, 3, 4]
        self.assertEqual(merge_sort(arr), [1, 2, 3, 4])

    def test_reverse_sorted(self):
        """Test sorting a reverse sorted array."""
        arr = [4, 3, 2, 1]
        self.assertEqual(merge_sort(arr), [1, 2, 3, 4])

    def test_large_array(self):
        """Test sorting a large array."""
        import random
        arr = [random.randint(-1000, 1000) for _ in range(1000)]
        sorted_arr = sorted(arr)
        self.assertEqual(merge_sort(arr), sorted_arr)

if __name__ == "__main__":
    unittest.main()