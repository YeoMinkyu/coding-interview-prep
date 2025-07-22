import unittest
from typing import Dict, List, Tuple

# Assuming your prims_mst implementation is in a module named graph_algorithms
# Adjust the import path based on your project structure
from data_structures.graph.prims_mst import prims_mst  # Replace with actual module path

class TestPrimsMST(unittest.TestCase):
    def setUp(self):
        """Set up a fresh environment for each test."""
        self.graph = None

    def test_simple_connected_graph(self):
        """Test Prim's algorithm on a simple connected graph."""
        self.graph = {
            0: [(1, 4), (2, 8)],
            1: [(0, 4), (2, 2), (3, 5)],
            2: [(0, 8), (1, 2), (3, 5)],
            3: [(1, 5), (2, 5)]
        }
        expected = [(0, 1, 4), (1, 2, 2), (1, 3, 5)]
        result = prims_mst(self.graph)
        self.assertEqual(sorted(result), sorted(expected))

    def test_empty_graph(self):
        """Test Prim's algorithm on an empty graph."""
        self.graph = {}
        self.assertEqual(prims_mst(self.graph), [])

    def test_single_vertex(self):
        """Test Prim's algorithm on a graph with a single vertex."""
        self.graph = {0: []}
        self.assertEqual(prims_mst(self.graph), [])

    def test_linear_graph(self):
        """Test Prim's algorithm on a linear graph."""
        self.graph = {
            0: [(1, 1)],
            1: [(0, 1), (2, 2)],
            2: [(1, 2)]
        }
        expected = [(0, 1, 1), (1, 2, 2)]
        result = prims_mst(self.graph)
        self.assertEqual(sorted(result), sorted(expected))

    def test_complete_graph(self):
        """Test Prim's algorithm on a complete graph with multiple edge weights."""
        self.graph = {
            0: [(1, 1), (2, 3), (3, 6)],
            1: [(0, 1), (2, 3), (3, 2)],
            2: [(0, 3), (1, 3), (3, 4)],
            3: [(0, 6), (1, 2), (2, 4)]
        }
        expected = [(0, 1, 1), (1, 3, 2), (0, 2, 3)]
        result = prims_mst(self.graph)
        self.assertEqual(sorted(result), sorted(expected))

if __name__ == "__main__":
    unittest.main()