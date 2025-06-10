import unittest
from data_structures.sorting.radix_sort import radix_sort

class TestRadixSort(unittest.TestCase):
    def test_basic_sorting(self):
        """Test sorting a standard array."""
        arr = [170, 45, 75, 90]
        self.assertEqual(radix_sort(arr), [45, 75, 90, 170])

    def test_empty_array(self):
        """Test sorting an empty array."""
        arr = []
        self.assertEqual(radix_sort(arr), [])

    def test_single_element(self):
        """Test sorting a single-element array."""
        arr = [5]
        self.assertEqual(radix_sort(arr), [5])

    def test_duplicates(self):
        """Test sorting an array with duplicates."""
        arr = [45, 75, 45, 90]
        self.assertEqual(radix_sort(arr), [45, 45, 75, 90])

    def test_negative_numbers(self):
        """Test sorting an array with negative numbers."""
        arr = [-170, 45, -75, 90]
        self.assertEqual(radix_sort(arr), [-170, -75, 45, 90])

    def test_large_numbers(self):
        """Test sorting with large numbers."""
        arr = [1000000, 1, 500, 1]
        self.assertEqual(radix_sort(arr), [1, 1, 500, 1000000])

if __name__ == "__main__":
    unittest.main()