import unittest
from data_structures.trees.binary_search_trees import BinarySearchTree, Node
import io
import sys

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_insert_basic(self):
        """Test inserting values into an empty and non-empty tree."""
        self.bst.insert(5)
        self.assertEqual(self.bst.get_node_count(), 1)
        self.assertTrue(self.bst.is_in_tree(5))
        self.bst.insert(3)
        self.bst.insert(7)
        self.assertEqual(self.bst.get_node_count(), 3)
        self.assertTrue(self.bst.is_in_tree(3))
        self.assertTrue(self.bst.is_in_tree(7))

    def test_insert_duplicate(self):
        """Test inserting duplicate values (should be ignored)."""
        self.bst.insert(5)
        self.bst.insert(5)
        self.assertEqual(self.bst.get_node_count(), 1)
        self.bst.insert(3)
        self.bst.insert(3)
        self.assertEqual(self.bst.get_node_count(), 2)

    def test_insert_unbalanced(self):
        """Test inserting into an unbalanced tree."""
        values = [10, 15, 20, 25]  # Right-skewed tree
        for v in values:
            self.bst.insert(v)
        self.assertEqual(self.bst.get_node_count(), 4)
        self.assertEqual(self.bst.get_height(), 4)
        self.assertTrue(self.bst.is_binary_search_tree())

    def test_get_node_count(self):
        """Test node count for empty and non-empty trees."""
        self.assertEqual(self.bst.get_node_count(), 0)
        self.bst.insert(5)
        self.assertEqual(self.bst.get_node_count(), 1)
        self.bst.insert(3)
        self.bst.insert(7)
        self.assertEqual(self.bst.get_node_count(), 3)

    def test_print_values(self):
        """Test printing values in ascending order."""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.bst.print_values()  # Empty tree
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "")

        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.bst.print_values()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "3\n5\n7")

    def test_delete_tree(self):
        """Test deleting the entire tree."""
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.delete_tree()
        self.assertEqual(self.bst.get_node_count(), 0)
        self.assertFalse(self.bst.is_in_tree(5))

    def test_is_in_tree(self):
        """Test searching for values in the tree."""
        self.assertFalse(self.bst.is_in_tree(5))
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.assertTrue(self.bst.is_in_tree(5))
        self.assertTrue(self.bst.is_in_tree(3))
        self.assertFalse(self.bst.is_in_tree(4))

    def test_get_height(self):
        """Test height for various tree configurations."""
        self.assertEqual(self.bst.get_height(), 0)
        self.bst.insert(5)
        self.assertEqual(self.bst.get_height(), 1)
        self.bst.insert(3)
        self.bst.insert(7)
        self.assertEqual(self.bst.get_height(), 2)
        self.bst.insert(2)
        self.assertEqual(self.bst.get_height(), 3)

    def test_get_min_max(self):
        """Test minimum and maximum values."""
        with self.assertRaises(ValueError):
            self.bst.get_min()
        with self.assertRaises(ValueError):
            self.bst.get_max()
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.assertEqual(self.bst.get_min(), 3)
        self.assertEqual(self.bst.get_max(), 7)

    def test_is_binary_search_tree(self):
        """Test BST validity."""
        self.assertTrue(self.bst.is_binary_search_tree())  # Empty tree
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.assertTrue(self.bst.is_binary_search_tree())
        # Create invalid BST
        self.bst = BinarySearchTree()
        self.bst.root = Node(5)
        self.bst.root.left = Node(6)  # Invalid: 6 > 5
        self.assertFalse(self.bst.is_binary_search_tree())

    def test_delete_value_leaf(self):
        """Test deleting a leaf node."""
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.delete_value(3)
        self.assertFalse(self.bst.is_in_tree(3))
        self.assertEqual(self.bst.get_node_count(), 2)
        self.assertTrue(self.bst.is_binary_search_tree())

    def test_delete_value_one_child(self):
        """Test deleting a node with one child."""
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(4)
        self.bst.delete_value(3)
        self.assertFalse(self.bst.is_in_tree(3))
        self.assertTrue(self.bst.is_in_tree(4))
        self.assertEqual(self.bst.get_node_count(), 2)

    def test_delete_value_two_children(self):
        """Test deleting a node with two children."""
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(6)
        self.bst.insert(8)
        self.bst.delete_value(7)
        self.assertFalse(self.bst.is_in_tree(7))
        self.assertTrue(self.bst.is_in_tree(6))
        self.assertEqual(self.bst.get_node_count(), 4)
        self.assertTrue(self.bst.is_binary_search_tree())

    def test_delete_root(self):
        """Test deleting the root node."""
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.delete_value(5)
        self.assertFalse(self.bst.is_in_tree(5))
        self.assertEqual(self.bst.get_node_count(), 2)
        self.assertTrue(self.bst.is_binary_search_tree())

    def test_delete_non_existent(self):
        """Test deleting a value not in the tree."""
        self.bst.insert(5)
        self.bst.delete_value(4)
        self.assertEqual(self.bst.get_node_count(), 1)

    def test_get_successor(self):
        """Test finding the successor for various cases."""
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(2)
        self.bst.insert(4)
        self.bst.insert(6)
        self.bst.insert(8)
        self.assertEqual(self.bst.get_successor(3), 4)
        self.assertEqual(self.bst.get_successor(7), 8)
        self.assertEqual(self.bst.get_successor(8), -1)
        self.assertEqual(self.bst.get_successor(1), 2)  # Not in tree
        self.assertEqual(self.bst.get_successor(5), 6)

    def test_get_successor_empty(self):
        """Test successor in an empty tree."""
        self.assertEqual(self.bst.get_successor(5), -1)

    def test_complex_tree_operations(self):
        """Test a sequence of operations on a complex tree."""
        values = [10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8]
        for v in values:
            self.bst.insert(v)
        self.assertEqual(self.bst.get_node_count(), 11)
        self.assertEqual(self.bst.get_height(), 4)
        self.assertEqual(self.bst.get_min(), 1)
        self.assertEqual(self.bst.get_max(), 18)
        self.bst.delete_value(5)
        self.assertFalse(self.bst.is_in_tree(5))
        self.bst.print_values()
        self.assertEqual(self.bst.get_node_count(), 10)
        self.assertTrue(self.bst.is_binary_search_tree())
        self.assertEqual(self.bst.get_successor(4), 6)

if __name__ == "__main__":
    unittest.main()