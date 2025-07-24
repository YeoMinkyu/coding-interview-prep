import unittest
from data_structures.graph.dijkstra import dijkstra  # Adjust path as needed

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        """Set up a fresh environment for each test."""
        self.graph = None
        self.source = None

    def test_simple_connected_graph(self):
        """Test Dijkstra on a simple connected graph."""
        self.graph = {
            0: [(1, 4), (2, 2)],
            1: [(3, 3)],
            2: [(1, 1), (3, 5)],
            3: []
        }
        self.source = 0
        self.assertEqual(dijkstra(self.graph, self.source), {0: 0, 1: 3, 2: 2, 3: 6})

    def test_disconnected_graph(self):
        """Test Dijkstra on a disconnected graph."""
        self.graph = {
            0: [(1, 5)],
            1: [],
            2: [(3, 2)],
            3: []
        }
        self.source = 0
        self.assertEqual(dijkstra(self.graph, self.source), {0: 0, 1: 5, 2: float('inf'), 3: float('inf')})

    def test_empty_graph(self):
        """Test Dijkstra on an empty graph."""
        self.graph = {}
        self.source = 0
        self.assertEqual(dijkstra(self.graph, self.source), {})

    def test_single_node(self):
        """Test Dijkstra on a graph with a single node."""
        self.graph = {0: []}
        self.source = 0
        self.assertEqual(dijkstra(self.graph, self.source), {0: 0})

    def test_complex_graph(self):
        """Test Dijkstra on a complex graph (simulating hotel network)."""
        self.graph = {
            0: [(1, 10), (2, 5)],
            1: [(3, 2), (4, 8)],
            2: [(1, 3), (4, 2)],
            3: [(4, 1)],
            4: []
        }
        self.source = 0
        expected = {0: 0, 1: 8, 2: 5, 3: 10, 4: 7}  # e.g., 0 -> 2 -> 4 (7) is shorter than 0 -> 1 -> 4 (18)
        self.assertEqual(dijkstra(self.graph, self.source), expected)

    def test_invalid_source(self):
        """Test Dijkstra with an invalid source node."""
        self.graph = {
            0: [(1, 4)],
            1: []
        }
        self.source = 2  # Invalid source (out of range)
        self.assertEqual(dijkstra(self.graph, self.source), {})

if __name__ == "__main__":
    unittest.main()