import unittest
from data_structures.graph.bellman_ford import bellman_ford  # Adjust path as needed

class TestBellmanFord(unittest.TestCase):
    def setUp(self):
        """Set up a fresh environment for each test."""
        self.edges = None
        self.num_vertices = None
        self.source = None

    def test_empty_graph(self):
        """Test Bellman-Ford on an empty graph."""
        self.edges = []
        self.num_vertices = 0
        self.source = 0
        self.assertEqual(bellman_ford(self.edges, self.num_vertices, self.source), ({}, False))

    def test_invalid_source(self):
        """Test Bellman-Ford with an invalid source node."""
        self.edges = [(0, 1, 4), (1, 2, 3)]
        self.num_vertices = 3
        self.source = 3  # Out of range
        self.assertEqual(bellman_ford(self.edges, self.num_vertices, self.source), ({}, False))

    def test_single_node_no_edges(self):
        """Test Bellman-Ford on a single node with no edges."""
        self.edges = []
        self.num_vertices = 1
        self.source = 0
        self.assertEqual(bellman_ford(self.edges, self.num_vertices, self.source), ({0: 0}, False))

    def test_simple_graph_with_positive_weights(self):
        """Test Bellman-Ford on a simple graph with positive weights."""
        self.edges = [(0, 1, 4), (0, 2, 2), (1, 3, 3), (2, 1, 1), (2, 3, 5)]
        self.num_vertices = 4
        self.source = 0
        self.assertEqual(bellman_ford(self.edges, self.num_vertices, self.source), ({0: 0, 1: 3, 2: 2, 3: 6}, False))

    def test_graph_with_negative_weights(self):
        """Test Bellman-Ford on a graph with negative weights."""
        self.edges = [(0, 1, 4), (0, 2, 3), (1, 2, -2), (2, 3, 1)]
        self.num_vertices = 4
        self.source = 0
        self.assertEqual(bellman_ford(self.edges, self.num_vertices, self.source), ({0: 0, 1: 4, 2: 2, 3: 3}, False))

    def test_graph_with_negative_cycle(self):
        """Test Bellman-Ford on a graph with a negative cycle."""
        self.edges = [(0, 1, 1), (1, 2, 1), (2, 0, -3)]
        self.num_vertices = 3
        self.source = 0
        self.assertEqual(bellman_ford(self.edges, self.num_vertices, self.source), ({0: 0, 1: 1, 2: 2}, True))

    def test_disconnected_graph(self):
        """Test Bellman-Ford on a disconnected graph."""
        self.edges = [(0, 1, 5), (2, 3, 2)]
        self.num_vertices = 4
        self.source = 0
        self.assertEqual(bellman_ford(self.edges, self.num_vertices, self.source), ({0: 0, 1: 5, 2: float('inf'), 3: float('inf')}, False))

    def test_dense_graph_with_mixed_weights(self):
        """Test Bellman-Ford on a dense graph with mixed positive and negative weights."""
        self.edges = [
            (0, 1, 10), (0, 2, 5), (1, 3, -2), (1, 4, 8),
            (2, 1, 3), (2, 4, -1), (3, 4, 1), (4, 0, 2)
        ]
        self.num_vertices = 5
        self.source = 0
        expected = {0: 0, 1: 5, 2: 5, 3: 3, 4: 2}  # e.g., 0 -> 2 -> 4 -> 0, but no negative cycle
        self.assertEqual(bellman_ford(self.edges, self.num_vertices, self.source), (expected, False))

    def test_duplicate_edges(self):
        """Test Bellman-Ford with duplicate edges (should use minimum weight)."""
        self.edges = [(0, 1, 4), (0, 1, 2), (1, 2, 3)]
        self.num_vertices = 3
        self.source = 0
        self.assertEqual(bellman_ford(self.edges, self.num_vertices, self.source), ({0: 0, 1: 2, 2: 5}, False))

    def test_self_loop(self):
        """Test Bellman-Ford with a self-loop (should be ignored for shortest path)."""
        self.edges = [(0, 0, 1), (0, 1, 3), (1, 2, 2)]
        self.num_vertices = 3
        self.source = 0
        self.assertEqual(bellman_ford(self.edges, self.num_vertices, self.source), ({0: 0, 1: 3, 2: 5}, False))

if __name__ == "__main__":
    unittest.main()