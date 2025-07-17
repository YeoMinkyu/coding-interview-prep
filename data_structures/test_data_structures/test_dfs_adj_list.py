import unittest

# Assuming your DFS implementation is in a module named dfs_adj_list
# Adjust the import path based on your project structure
from data_structures.graph.dfs_adj_list import dfs_recursive, dfs_iterative, has_cycle  # Replace with actual module path

class TestDFS(unittest.TestCase):
    def setUp(self):
        """Set up a fresh environment for each test."""
        self.graph = None

    def test_basic_traversal(self):
        """Test recursive DFS on a standard connected graph."""
        self.graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
        self.assertEqual(dfs_recursive(self.graph, 0), [0, 1, 3, 2])
        self.assertEqual(dfs_iterative(self.graph, 0), [0, 1, 3, 2])

    def test_empty_graph(self):
        """Test recursive DFS on an empty graph."""
        self.graph = {}
        self.assertEqual(dfs_recursive(self.graph, 0), [])
        self.assertEqual(dfs_iterative(self.graph, 0), [])

    def test_invalid_start_node(self):
        """Test recursive DFS with an invalid start node."""
        self.graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
        self.assertEqual(dfs_recursive(self.graph, 4), [])
        self.assertEqual(dfs_iterative(self.graph, 4), [])

    def test_single_node(self):
        """Test recursive DFS on a graph with a single node."""
        self.graph = {0: []}
        self.assertEqual(dfs_recursive(self.graph, 0), [0])
        self.assertEqual(dfs_iterative(self.graph, 0), [0])

    def test_disconnected_graph(self):
        """Test recursive DFS on a disconnected graph."""
        self.graph = {0: [1], 1: [0, 2], 2: [1], 3: []}
        self.assertEqual(dfs_recursive(self.graph, 2), [2, 1, 0])
        self.assertEqual(dfs_iterative(self.graph, 2), [2, 1, 0])

    def test_cycle(self):
        """Test recursive DFS on a graph with a cycle."""
        self.graph = {0: [1], 1: [0, 2], 2: [1]}
        self.assertEqual(dfs_recursive(self.graph, 0), [0, 1, 2])
        self.assertEqual(dfs_iterative(self.graph, 0), [0, 1, 2])

    def test_large_graph(self):
        """Test recursive DFS on a larger graph."""
        self.graph = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3]}
        self.assertEqual(dfs_recursive(self.graph, 0), [0, 1, 2, 3, 4])
        self.assertEqual(dfs_iterative(self.graph, 0), [0, 1, 2, 3, 4])
    
    def test_graph_with_cycle(self):
        """Test has_cycle on a graph with a cycle (triangle)."""
        self.graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3]}
        self.assertTrue(has_cycle(self.graph, 0))

    def test_acyclic_graph(self):
        """Test has_cycle on a tree (acyclic graph)."""
        self.graph = {0: [1, 3], 1: [0, 2], 2: [1], 3: [0]}
        self.assertFalse(has_cycle(self.graph, 0))

    def test_empty_graph(self):
        """Test has_cycle on an empty graph."""
        self.graph = {}
        self.assertFalse(has_cycle(self.graph, 0))

    def test_single_node(self):
        """Test has_cycle on a graph with a single node."""
        self.graph = {0: []}
        self.assertFalse(has_cycle(self.graph, 0))

    def test_disconnected_graph_with_cycle(self):
        """Test has_cycle on a disconnected graph where the reachable component has a cycle."""
        self.graph = {0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [4], 4: [3]}
        self.assertTrue(has_cycle(self.graph, 0))

    def test_path_with_cycle(self):
        """Test has_cycle on a linear path that loops back to form a cycle."""
        self.graph = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 0]}
        self.assertTrue(has_cycle(self.graph, 0))

if __name__ == "__main__":
    unittest.main()