import unittest
from data_structures.graph.bfs_adj_matrix import bfs_adj_matrix  # Adjust path as needed

class TestBFSAdjMatrix(unittest.TestCase):
    def test_basic_sorting(self):
        """Test BFS on a standard connected graph."""
        graph = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
        self.assertEqual(bfs_adj_matrix(graph, 0), [0, 1, 2, 3])

    def test_empty_graph(self):
        """Test BFS on an empty graph."""
        graph = []
        self.assertEqual(bfs_adj_matrix(graph, 0), [])

    def test_invalid_start_node(self):
        """Test BFS with an invalid start node."""
        graph = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
        self.assertEqual(bfs_adj_matrix(graph, 4), [])

    def test_single_node(self):
        """Test BFS on a graph with a single node."""
        graph = [[0]]
        self.assertEqual(bfs_adj_matrix(graph, 0), [0])

    def test_disconnected_graph(self):
        """Test BFS on a disconnected graph."""
        graph = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
        self.assertEqual(bfs_adj_matrix(graph, 0), [0, 1])  # Only visits connected component

    def test_cycle(self):
        """Test BFS on a graph with a cycle."""
        graph = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        self.assertEqual(bfs_adj_matrix(graph, 0), [0, 1, 2])

    def test_large_graph(self):
        """Test BFS on a larger graph (simulating hotel network)."""
        graph = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0]]
        self.assertEqual(bfs_adj_matrix(graph, 0), [0, 1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()