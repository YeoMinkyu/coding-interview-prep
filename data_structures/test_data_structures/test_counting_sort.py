import unittest
from data_structures.sorting.counting_sort import counting_sort

class TestCountingSort(unittest.TestCase):
    def test_basic_sorting(self):
        """Test sorting a standard array."""
        arr = [3, 1, 4, 1]
        self.assertEqual(counting_sort(arr, 1, 4), [1, 1, 3, 4])

    def test_empty_array(self):
        """Test sorting an empty array."""
        arr = []
        self.assertEqual(counting_sort(arr, 0, 0), [])

    def test_single_element(self):
        """Test sorting a single-element array."""
        arr = [5]
        self.assertEqual(counting_sort(arr, 5, 5), [5])

    def test_duplicates(self):
        """Test sorting an array with duplicates."""
        arr = [5, 2, 5, 1, 2]
        self.assertEqual(counting_sort(arr, 1, 5), [1, 2, 2, 5, 5])

    def test_negative_numbers(self):
        """Test sorting an array with negative numbers."""
        arr = [-3, 1, -5, 2, -1]
        self.assertEqual(counting_sort(arr, -5, 2), [-5, -3, -1, 1, 2])

    def test_large_range(self):
        """Test sorting with a large range."""
        arr = [100, 1, 50, 1]
        self.assertEqual(counting_sort(arr, 1, 100), [1, 1, 50, 100])

if __name__ == "__main__":
    unittest.main()