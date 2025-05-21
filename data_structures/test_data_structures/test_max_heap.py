import unittest
from data_structures.heap.max_heap import MaxHeap

class TestMaxHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MaxHeap()

    def test_insert_basic(self):
        """Test inserting values into an empty and non-empty heap."""
        self.heap.insert(5)
        self.assertEqual(self.heap.get_size(), 1)
        self.assertEqual(self.heap.get_max(), 5)
        self.heap.insert(3)
        self.heap.insert(7)
        self.assertEqual(self.heap.get_size(), 3)
        self.assertEqual(self.heap.get_max(), 7)
        self.assertEqual(self.heap.heap, [7, 3, 5])

    def test_insert_duplicates(self):
        """Test inserting duplicate values."""
        self.heap.insert(5)
        self.heap.insert(5)
        self.heap.insert(5)
        self.assertEqual(self.heap.get_size(), 3)
        self.assertEqual(self.heap.get_max(), 5)
        self.assertEqual(self.heap.extract_max(), 5)
        self.assertEqual(self.heap.get_size(), 2)
        self.assertEqual(self.heap.get_max(), 5)

    def test_insert_negative_numbers(self):
        """Test inserting negative numbers."""
        self.heap.insert(-1)
        self.heap.insert(-5)
        self.heap.insert(-3)
        self.assertEqual(self.heap.get_size(), 3)
        self.assertEqual(self.heap.get_max(), -1)
        self.assertEqual(self.heap.extract_max(), -1)
        self.assertEqual(self.heap.get_max(), -3)

    def test_insert_extreme_values(self):
        """Test inserting maximum and minimum 32-bit integers."""
        max_int = 2**31 - 1  # 2147483647
        min_int = -2**31     # -2147483648
        self.heap.insert(max_int)
        self.heap.insert(min_int)
        self.heap.insert(0)
        self.assertEqual(self.heap.get_size(), 3)
        self.assertEqual(self.heap.get_max(), max_int)
        self.assertEqual(self.heap.extract_max(), max_int)
        self.assertEqual(self.heap.get_max(), 0)

    def test_insert_large_heap(self):
        """Test inserting many elements to create a large heap."""
        for i in range(1000):
            self.heap.insert(i)
        self.assertEqual(self.heap.get_size(), 1000)
        self.assertEqual(self.heap.get_max(), 999)
        self.assertEqual(self.heap.extract_max(), 999)
        self.assertEqual(self.heap.get_size(), 999)

    def test_get_max(self):
        """Test getting the maximum value."""
        with self.assertRaises(ValueError):
            self.heap.get_max()
        self.heap.insert(5)
        self.assertEqual(self.heap.get_max(), 5)
        self.heap.insert(7)
        self.assertEqual(self.heap.get_max(), 7)
        self.heap.insert(3)
        self.assertEqual(self.heap.get_max(), 7)

    def test_get_size(self):
        """Test size of the heap."""
        self.assertEqual(self.heap.get_size(), 0)
        self.heap.insert(5)
        self.assertEqual(self.heap.get_size(), 1)
        self.heap.insert(3)
        self.assertEqual(self.heap.get_size(), 2)
        self.heap.extract_max()
        self.assertEqual(self.heap.get_size(), 1)

    def test_is_empty(self):
        """Test empty heap check."""
        self.assertTrue(self.heap.is_empty())
        self.heap.insert(5)
        self.assertFalse(self.heap.is_empty())
        self.heap.extract_max()
        self.assertTrue(self.heap.is_empty())

    def test_extract_max_single_element(self):
        """Test extracting max from a single-element heap."""
        self.heap.insert(5)
        self.assertEqual(self.heap.extract_max(), 5)
        self.assertEqual(self.heap.get_size(), 0)
        self.assertTrue(self.heap.is_empty())
        with self.assertRaises(ValueError):
            self.heap.extract_max()

    def test_extract_max_multiple(self):
        """Test extracting max multiple times."""
        values = [5, 3, 7, 2, 8, 1]
        for v in values:
            self.heap.insert(v)
        self.assertEqual(self.heap.extract_max(), 8)
        self.assertEqual(self.heap.get_size(), 5)
        self.assertEqual(self.heap.get_max(), 7)
        self.assertEqual(self.heap.extract_max(), 7)
        self.assertEqual(self.heap.get_size(), 4)
        self.assertEqual(self.heap.get_max(), 5)

    def test_extract_max_unbalanced(self):
        """Test extracting max from an unbalanced heap (e.g., left-heavy)."""
        values = [10, 9, 8, 7, 6]  # Left-heavy heap
        for v in values:
            self.heap.insert(v)
        self.assertEqual(self.heap.extract_max(), 10)
        self.assertEqual(self.heap.get_size(), 4)
        self.assertEqual(self.heap.get_max(), 9)
        self.assertEqual(self.heap.heap[:4], [9, 7, 8, 6])

    def test_sift_up_edge_cases(self):
        """Test sift_up with edge cases (root, single element)."""
        self.heap.insert(5)
        self.heap.sift_up(0)  # Root
        self.assertEqual(self.heap.get_max(), 5)
        self.heap.insert(7)
        self.heap.sift_up(1)  # Should swap with root
        self.assertEqual(self.heap.get_max(), 7)
        self.assertEqual(self.heap.heap, [7, 5])

    def test_sift_down_edge_cases(self):
        """Test sift_down with edge cases (leaf, single element)."""
        self.heap.insert(5)
        self.heap.sift_down(0)  # Single element
        self.assertEqual(self.heap.get_max(), 5)
        self.heap.insert(3)
        self.heap.insert(2)
        self.heap.heap[0] = 1  # Force sift down
        self.heap.sift_down(0)
        self.assertEqual(self.heap.get_max(), 3)
        self.assertEqual(self.heap.heap, [3, 1, 2])

    def test_complex_operations(self):
        """Test a complex sequence of insertions and extractions."""
        values = [10, 5, 15, 3, 7, 12, 18, 1, 4, 6]
        for v in values:
            self.heap.insert(v)
        self.assertEqual(self.heap.get_size(), 10)
        self.assertEqual(self.heap.get_max(), 18)
        self.assertEqual(self.heap.extract_max(), 18)
        self.assertEqual(self.heap.get_max(), 15)
        self.assertEqual(self.heap.extract_max(), 15)
        self.assertEqual(self.heap.get_size(), 8)
        self.heap.insert(20)
        self.assertEqual(self.heap.get_max(), 20)
        self.assertEqual(self.heap.get_size(), 9)

    def test_stress_test(self):
        """Stress test with many insertions and extractions."""
        import random
        values = list(range(10))
        random.shuffle(values)
        for v in values:
            self.heap.insert(v)
        self.assertEqual(self.heap.get_size(), 10)
        sorted_values = sorted(values, reverse=True)
        for i in range(10):
            self.assertEqual(self.heap.extract_max(), sorted_values[i])
        self.assertTrue(self.heap.is_empty())

    def test_remove(self):
        """Test removing elements by index."""
        self.heap.insert(5)
        self.heap.insert(3)
        self.heap.insert(7)
        self.heap.remove(1)  # Remove 3
        self.assertEqual(self.heap.get_size(), 2)
        self.assertEqual(self.heap.get_max(), 7)
        with self.assertRaises(ValueError):
            self.heap.remove(10)  # Invalid index

    def test_heapify(self):
        """Test converting an array into a max-heap."""
        array = [3, 1, 4, 2]
        self.heap.heapify(array)
        self.assertEqual(self.heap.get_size(), 4)
        self.assertEqual(self.heap.get_max(), 4)
        self.assertEqual(self.heap.extract_max(), 4)

    def test_heap_sort(self):
        """Test sorting an array using heap sort."""
        array = [3, 1, 4, 2]
        self.heap.heap_sort(array)
        self.assertEqual(array, [1, 2, 3, 4])
        array = []
        self.heap.heap_sort(array)
        self.assertEqual(array, [])
        array = [1]
        self.heap.heap_sort(array)
        self.assertEqual(array, [1])

    def test_complex_operations(self):
        """Test a sequence of operations on a complex heap."""
        values = [10, 5, 15, 3, 7, 12, 18]
        for v in values:
            self.heap.insert(v)
        self.assertEqual(self.heap.get_size(), 7)
        self.assertEqual(self.heap.get_max(), 18)
        self.assertEqual(self.heap.extract_max(), 18)
        self.assertEqual(self.heap.get_size(), 6)
        self.heap.remove(0)  # Remove new max
        self.assertEqual(self.heap.get_size(), 5)
        array = [3, 1, 4, 2]
        self.heap.heapify(array)
        self.heap.heap_sort(array)
        self.assertEqual(array, [1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()