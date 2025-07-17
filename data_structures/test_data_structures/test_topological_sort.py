import unittest
from data_structures.graph.topological_sort import topological_sort  # Adjust path as needed

class TestTopologicalSort(unittest.TestCase):
    def setUp(self):
        """Set up a fresh environment for each test."""
        self.graph = None

    def test_basic_dag(self):
        """Test topological sort on a simple DAG."""
        self.graph = {0: [1], 1: [2], 2: []}
        self.assertEqual(topological_sort(self.graph), [0, 1, 2])

    def test_empty_graph(self):
        """Test topological sort on an empty graph."""
        self.graph = {}
        self.assertEqual(topological_sort(self.graph), [])

    def test_single_node(self):
        """Test topological sort on a graph with a single node."""
        self.graph = {0: []}
        self.assertEqual(topological_sort(self.graph), [0])

    def test_disconnected_components(self):
        """Test topological sort on a DAG with disconnected components."""
        self.graph = {0: [1], 1: [], 2: [3], 3: []}
        result = topological_sort(self.graph)
        self.assertTrue(set(result) == {0, 1, 2, 3})
        self.assertTrue(all(result.index(u) < result.index(v) for u, v in [(0, 1), (2, 3)]))

    def test_complex_dag(self):
        """Test topological sort on a complex DAG (simulating task dependencies)."""
        self.graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        result = topological_sort(self.graph)
        self.assertTrue(set(result) == {0, 1, 2, 3})
        self.assertTrue(result.index(0) < result.index(1) and result.index(0) < result.index(2))
        self.assertTrue(result.index(1) < result.index(3) and result.index(2) < result.index(3))

    def test_cycle_detection(self):
        """Test topological sort on a graph with a cycle (should handle or raise)."""
        self.graph = {0: [1], 1: [2], 2: [0]}
        # Note: A true topological sort requires a DAG. Implementations may return [] or raise an exception.
        result = topological_sort(self.graph)
        self.assertEqual(result, [])  # Assuming empty list for cycles
        self.graph = {0: [1, 2], 1: [2, 3], 2: [3], 3: []}
        result = topological_sort(self.graph)
        self.assertEqual(result, [0, 1, 2, 3])

if __name__ == "__main__":
    unittest.main()