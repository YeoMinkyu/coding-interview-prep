import unittest
from data_structures.binary_search.binary_search import BinarySearch

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        """Initialize the BinarySearch object before each test."""
        self.bs = BinarySearch()

    # Test iterative binary_search
    def test_binary_search_found(self):
        """Test iterative binary search when target is found."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(self.bs.binary_search(arr, 3), 2)
        self.assertEqual(self.bs.binary_search(arr, 1), 0)
        self.assertEqual(self.bs.binary_search(arr, 5), 4)

    def test_binary_search_not_found(self):
        """Test iterative binary search when target is not found."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(self.bs.binary_search(arr, 6), -1)
        self.assertEqual(self.bs.binary_search(arr, 0), -1)

    def test_binary_search_empty(self):
        """Test iterative binary search on an empty array."""
        arr = []
        self.assertEqual(self.bs.binary_search(arr, 1), -1)

    def test_binary_search_single_element(self):
        """Test iterative binary search on a single-element array."""
        arr = [1]
        self.assertEqual(self.bs.binary_search(arr, 1), 0)
        self.assertEqual(self.bs.binary_search(arr, 2), -1)

    def test_binary_search_duplicates(self):
        """Test iterative binary search with duplicate values."""
        arr = [1, 2, 2, 2, 3]
        self.assertIn(self.bs.binary_search(arr, 2), [1, 2, 3])  # Any index of 2 is valid

    # Test recursive binary_search_recursive
    def test_binary_search_recursive_found(self):
        """Test recursive binary search when target is found."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(self.bs.binary_search_recursive(arr, 3), 2)
        self.assertEqual(self.bs.binary_search_recursive(arr, 1), 0)
        self.assertEqual(self.bs.binary_search_recursive(arr, 5), 4)

    def test_binary_search_recursive_not_found(self):
        """Test recursive binary search when target is not found."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(self.bs.binary_search_recursive(arr, 6), -1)
        self.assertEqual(self.bs.binary_search_recursive(arr, 0), -1)

    def test_binary_search_recursive_empty(self):
        """Test recursive binary search on an empty array."""
        arr = []
        self.assertEqual(self.bs.binary_search_recursive(arr, 1), -1)

    def test_binary_search_recursive_single_element(self):
        """Test recursive binary search on a single-element array."""
        arr = [1]
        self.assertEqual(self.bs.binary_search_recursive(arr, 1), 0)
        self.assertEqual(self.bs.binary_search_recursive(arr, 2), -1)

    def test_binary_search_recursive_duplicates(self):
        """Test recursive binary search with duplicate values."""
        arr = [1, 2, 2, 2, 3]
        self.assertIn(self.bs.binary_search_recursive(arr, 2), [1, 2, 3])  # Any index of 2 is valid

if __name__ == "__main__":
    unittest.main()