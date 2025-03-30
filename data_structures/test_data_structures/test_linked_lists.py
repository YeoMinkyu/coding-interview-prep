
import unittest
from data_structures.linkedlists.linked_lists import LinkedList

"""
Test Cases by XAi
"""
class TestLinkedList(unittest.TestCase):
    def setUp(self):
        """Initialize a new LinkedList before each test."""
        self.ll = LinkedList()

    # Test size()
    def test_size_empty(self):
        """Test size of an empty list."""
        self.assertEqual(self.ll.size, 0)

    def test_size_non_empty(self):
        """Test size after adding elements."""
        self.ll.push_front(1)
        self.ll.push_front(2)
        self.ll.push_front(3)
        self.assertEqual(self.ll.size, 3)

    # Test empty()
    def test_empty_true(self):
        """Test empty() on an empty list."""
        self.assertTrue(self.ll.empty)

    def test_empty_false(self):
        """Test empty() on a non-empty list."""
        self.ll.push_back(1)
        self.assertFalse(self.ll.empty)

    # Test value_at()
    def test_value_at(self):
        """Test retrieving values at various indices."""
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)
        self.assertEqual(self.ll.value_at(0), 1)
        self.assertEqual(self.ll.value_at(1), 2)
        self.assertEqual(self.ll.value_at(2), 3)

    def test_value_at_invalid_index(self):
        """Test value_at() with invalid indices."""
        self.ll.push_back(1)
        with self.assertRaises(IndexError):
            self.ll.value_at(-1)  # Negative index
        with self.assertRaises(IndexError):
            self.ll.value_at(1)   # Beyond size

    # Test push_front()
    def test_push_front_empty(self):
        """Test push_front() on an empty list."""
        self.ll.push_front(5)
        self.assertEqual(self.ll.size, 1)
        self.assertEqual(self.ll.head.value, 5)

    def test_push_front_non_empty(self):
        """Test push_front() on a non-empty list."""
        self.ll.push_front(1)
        self.ll.push_front(2)
        self.assertEqual(self.ll.size, 2)
        self.assertEqual(self.ll.head.value, 2)
        self.assertEqual(self.ll.head.next.value, 1)

    # Test pop_front()
    def test_pop_front_empty(self):
        """Test pop_front() on an empty list."""
        with self.assertRaises(ValueError):
            self.ll.pop_front()

    def test_pop_front_single(self):
        """Test pop_front() on a single-node list."""
        self.ll.push_front(1)
        value = self.ll.pop_front()
        self.assertEqual(value, 1)
        self.assertTrue(self.ll.empty)

    def test_pop_front_multiple(self):
        """Test pop_front() on a multi-node list."""
        self.ll.push_front(1)
        self.ll.push_front(2)
        value = self.ll.pop_front()
        self.assertEqual(value, 2)
        self.assertEqual(self.ll.size, 1)
        self.assertEqual(self.ll.head.value, 1)

    # Test push_back()
    def test_push_back_empty(self):
        """Test push_back() on an empty list."""
        self.ll.push_back(5)
        self.assertEqual(self.ll.size, 1)
        self.assertEqual(self.ll.head.value, 5)

    def test_push_back_non_empty(self):
        """Test push_back() on a non-empty list."""
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.assertEqual(self.ll.size, 2)
        self.assertEqual(self.ll.value_at(0), 1)
        self.assertEqual(self.ll.value_at(1), 2)

    # Test pop_back()
    def test_pop_back_empty(self):
        """Test pop_back() on an empty list."""
        with self.assertRaises(ValueError):
            self.ll.pop_back()

    def test_pop_back_single(self):
        """Test pop_back() on a single-node list."""
        self.ll.push_back(1)
        value = self.ll.pop_back()
        self.assertEqual(value, 1)
        self.assertTrue(self.ll.empty)

    def test_pop_back_multiple(self):
        """Test pop_back() on a multi-node list."""
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)
        value = self.ll.pop_back()
        self.assertEqual(value, 3)
        self.assertEqual(self.ll.size, 2)
        self.assertEqual(self.ll.value_at(1), 2)

    # Test front()
    def test_front_empty(self):
        """Test front() on an empty list."""
        with self.assertRaises(ValueError):
            self.ll.front()

    def test_front_non_empty(self):
        """Test front() on a non-empty list."""
        self.ll.push_front(1)
        self.ll.push_front(2)
        self.assertEqual(self.ll.front(), 2)

    # Test back()
    def test_back_empty(self):
        """Test back() on an empty list."""
        with self.assertRaises(ValueError):
            self.ll.back()

    def test_back_non_empty(self):
        """Test back() on a non-empty list."""
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.assertEqual(self.ll.back(), 2)

    # Test insert()
    def test_insert_empty(self):
        """Test insert() at index 0 in an empty list."""
        self.ll.insert(0, 5)
        self.assertEqual(self.ll.size, 1)
        self.assertEqual(self.ll.head.value, 5)

    def test_insert_at_head(self):
        """Test insert() at index 0 in a non-empty list."""
        self.ll.push_back(1)
        self.ll.insert(0, 2)
        self.assertEqual(self.ll.size, 2)
        self.assertEqual(self.ll.value_at(0), 2)
        self.assertEqual(self.ll.value_at(1), 1)

    def test_insert_middle(self):
        """Test insert() in the middle of the list."""
        self.ll.push_back(1)
        self.ll.push_back(3)
        self.ll.insert(1, 2)
        self.assertEqual(self.ll.size, 3)
        self.assertEqual(self.ll.value_at(0), 1)
        self.assertEqual(self.ll.value_at(1), 2)
        self.assertEqual(self.ll.value_at(2), 3)

    def test_insert_invalid_index(self):
        """Test insert() with invalid indices."""
        self.ll.push_back(1)
        with self.assertRaises(IndexError):
            self.ll.insert(-1, 2)  # Negative index
        with self.assertRaises(IndexError):
            self.ll.insert(2, 2)   # Beyond size

    # Test erase()
    def test_erase_empty(self):
        """Test erase() on an empty list."""
        with self.assertRaises(IndexError):
            self.ll.erase(0)

    def test_erase_single(self):
        """Test erase() on a single-node list."""
        self.ll.push_back(1)
        self.ll.erase(0)
        self.assertTrue(self.ll.empty)

    def test_erase_middle(self):
        """Test erase() in the middle of the list."""
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)
        self.ll.erase(1)
        self.assertEqual(self.ll.size, 2)
        self.assertEqual(self.ll.value_at(0), 1)
        self.assertEqual(self.ll.value_at(1), 3)

    def test_erase_invalid_index(self):
        """Test erase() with invalid indices."""
        self.ll.push_back(1)
        with self.assertRaises(IndexError):
            self.ll.erase(-1)  # Negative index
        with self.assertRaises(IndexError):
            self.ll.erase(1)   # Beyond size

    # Test value_n_from_end()
    def test_value_n_from_end_empty(self):
        """Test value_n_from_end() on an empty list."""
        with self.assertRaises(IndexError):
            self.ll.value_n_from_end(0)

    def test_value_n_from_end(self):
        """Test value_n_from_end() with valid n."""
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)
        self.assertEqual(self.ll.value_n_from_end(0), 3)  # Last node
        self.assertEqual(self.ll.value_n_from_end(1), 2)  # Second-to-last
        self.assertEqual(self.ll.value_n_from_end(2), 1)  # Third-to-last

    def test_value_n_from_end_invalid(self):
        """Test value_n_from_end() with invalid n."""
        self.ll.push_back(1)
        with self.assertRaises(IndexError):
            self.ll.value_n_from_end(-1)  # Negative n
        with self.assertRaises(IndexError):
            self.ll.value_n_from_end(1)   # Beyond size

    # Test reverse()
    def test_reverse_empty(self):
        """Test reverse() on an empty list."""
        with self.assertRaises(ValueError):
            self.ll.reverse()

    def test_reverse_single(self):
        """Test reverse() on a single-node list."""
        self.ll.push_back(1)
        self.ll.reverse()
        self.assertEqual(self.ll.size, 1)
        self.assertEqual(self.ll.head.value, 1)

    def test_reverse_multiple(self):
        """Test reverse() on a multi-node list."""
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)
        self.ll.reverse()
        self.assertEqual(self.ll.size, 3)
        self.assertEqual(self.ll.value_at(0), 3)
        self.assertEqual(self.ll.value_at(1), 2)
        self.assertEqual(self.ll.value_at(2), 1)

    # Test remove_value()
    def test_remove_value_empty(self):
        """Test remove_value() on an empty list."""
        with self.assertRaises(ValueError):
            self.ll.remove_value(1)

    def test_remove_value_not_found(self):
        """Test remove_value() when value is not found."""
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.remove_value(3)  # Not in list
        self.assertEqual(self.ll.size, 2)
        self.assertEqual(self.ll.value_at(0), 1)
        self.assertEqual(self.ll.value_at(1), 2)

    def test_remove_value_found(self):
        """Test remove_value() when value is found."""
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)
        self.ll.remove_value(2)
        self.assertEqual(self.ll.size, 2)
        self.assertEqual(self.ll.value_at(0), 1)
        self.assertEqual(self.ll.value_at(1), 3)

if __name__ == "__main__":
    unittest.main()


"""
Self-made Test Cases
"""

# class TestLinkedLists(unittest.TestCase):
#     def setUp(self):
#         self.linked_lists = LinkedList()

#     def test_empty(self):
#         self.assertTrue(self.linked_lists.empty)
#         self.linked_lists.push_front(10)
#         self.linked_lists.push_front(9)
#         self.assertFalse(self.linked_lists.empty)

#     def test_size(self):
#         self.assertEqual(self.linked_lists.size, 0)
        
#         self.linked_lists.push_front(10)
#         self.linked_lists.push_front(9)
#         self.linked_lists.push_front(8)

#         self.assertEqual(self.linked_lists.size, 3)
    
#     def test_value_at(self):
#         self.assertEqual(self.linked_lists.size, 0)

#         self.linked_lists.push_front(10)
#         self.linked_lists.push_front(9)
#         self.linked_lists.push_front(8)
        
#         self.assertEqual(self.linked_lists.size, 3)
#         self.assertEqual(self.linked_lists.value_at(0), 8)
#         self.assertEqual(self.linked_lists.value_at(1), 9)
#         self.assertEqual(self.linked_lists.value_at(2), 10)

#     def test_push_front(self):
#         self.linked_lists.push_front(10)

#         self.assertEqual(self.linked_lists.head.value, 10)
    
#     def test_pop_front(self):
#         input_size = 5
#         self.assertEqual(self.linked_lists.size, 0)

#         for num in range(input_size):
#             self.linked_lists.push_front(num)
        
#         for num in range(input_size - 1, -1, -1):
#             self.assertEqual(self.linked_lists.pop_front(), num)
        
#         with self.assertRaises(ValueError):
#             self.linked_lists.pop_front()
    
#     def test_push_back(self):
#         input_size = 5
#         self.assertEqual(self.linked_lists.size, 0)

#         for num in range(input_size):
#             self.linked_lists.push_back(num)
        
#         self.assertEqual(self.linked_lists.size, 5)
#         self.assertEqual(self.linked_lists.value_at(4), 4)
#         self.assertEqual(self.linked_lists.value_at(0), 0)
#         self.assertEqual(self.linked_lists.pop_front(), 0)
#         self.assertEqual(self.linked_lists.size, 4)

#     def test_pop_back(self):
#         input_size = 5
#         self.assertEqual(self.linked_lists.size, 0)

#         for num in range(input_size):
#             self.linked_lists.push_back(num)
        
#         for num in range(input_size -1, -1, -1):
#             self.assertEqual(self.linked_lists.pop_back(), num)
        
#         with self.assertRaises(ValueError):
#             self.linked_lists.pop_back()

#     def test_front(self):
#         input_size = 5
#         self.assertEqual(self.linked_lists.size, 0)

#         with self.assertRaises(ValueError):
#             self.linked_lists.front()

#         for num in range(input_size):
#             self.linked_lists.push_back(num)

#         self.assertEqual(self.linked_lists.front(), 0)

#         for num in range(3):
#             self.linked_lists.pop_front()

#         self.assertEqual(self.linked_lists.front(), 3)

#     def test_back(self):
#         input_size = 5
#         self.assertEqual(self.linked_lists.size, 0)

#         with self.assertRaises(ValueError):
#             self.linked_lists.back()

#         for num in range(input_size):
#             self.linked_lists.push_back(num)

#         self.assertEqual(self.linked_lists.back(), 4)

#         for num in range(3):
#             self.linked_lists.pop_back()

#         self.assertEqual(self.linked_lists.back(), 1)

#     def test_insert(self):
#         input_size = 5

#         with self.assertRaises(IndexError):
#             self.linked_lists.insert(0, 10)

#         for num in range(input_size):
#             self.linked_lists.push_back(num)

#         with self.assertRaises(IndexError):
#             self.linked_lists.insert(-1, 10)

#         self.linked_lists.insert(0, 10)
#         self.assertEqual(self.linked_lists.front(), 10)

#         self.assertEqual(self.linked_lists.size, 6)

#         self.linked_lists.insert(2, 12)

#         self.assertEqual(self.linked_lists.size, 7)
#         self.assertEqual(self.linked_lists.value_at(2), 12)

#     def test_erase(self):
#         input_size = 5

#         with self.assertRaises(IndexError):
#             self.linked_lists.erase(0)

#         for num in range(input_size):
#             self.linked_lists.push_back(num)

#         self.linked_lists.erase(0)
#         self.assertEqual(self.linked_lists.size, 4)
#         self.assertEqual(self.linked_lists.value_at(0), 1)
        

#         self.linked_lists.erase(3)
#         self.assertEqual(self.linked_lists.size, 3)
#         self.assertEqual(self.linked_lists.value_at(2), 3)

#         with self.assertRaises(IndexError):
#             self.linked_lists.value_at(3)
 
#     def test_value_n_from_end(self):
#         input_size = 5

#         for num in range(input_size):
#             self.linked_lists.push_back(num)

#         self.assertEqual(self.linked_lists.value_n_from_end(0), 4)
#         self.assertEqual(self.linked_lists.value_n_from_end(4), 0)
    
#     def test_reverse(self):
#         input_size = 5

#         for num in range(input_size):
#             self.linked_lists.push_back(num)
        
#         self.linked_lists.reverse()

#         for num in range(input_size-1, -1, -1):
#             self.assertEqual(self.linked_lists.pop_front(), num)
        
#     def test_remove_value(self):
#         input_size = 5

#         for num in range(input_size):
#             self.linked_lists.push_back(num)

#         self.linked_lists.remove_value(0)
#         self.assertEqual(self.linked_lists.size, 4)

#         self.linked_lists.remove_value(5)
#         self.assertEqual(self.linked_lists.size, 4)

# if __name__ == "__main__":
#     unittest.main()