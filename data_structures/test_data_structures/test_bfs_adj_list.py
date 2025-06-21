import unittest
from data_structures.graph.bfs_adj_list import BFS  # Adjusted path

class TestBFSAdjList(unittest.TestCase):
    def setUp(self):
        """Set up a fresh BFS instance for each test."""
        self.bfs = None

    def test_basic_sorting(self):
        """Test BFS on a standard connected graph."""
        self.bfs = BFS([[1, 2], [0, 3], [0], [1]])
        self.assertEqual(self.bfs.bfs_adj_list(0), [0, 1, 2, 3])

    def test_empty_graph(self):
        """Test BFS on an empty graph."""
        self.bfs = BFS([])
        self.assertEqual(self.bfs.bfs_adj_list(0), [])

    def test_invalid_start_node(self):
        """Test BFS with an invalid start node."""
        self.bfs = BFS([[1, 2], [0, 3], [0], [1]])
        self.assertEqual(self.bfs.bfs_adj_list(4), [])

    def test_single_node(self):
        """Test BFS on a graph with a single node."""
        self.bfs = BFS([[]])
        self.assertEqual(self.bfs.bfs_adj_list(0), [0])

    def test_disconnected_graph(self):
        """Test BFS on a disconnected graph."""
        self.bfs = BFS([[1], [0], [3], [2]])
        self.assertEqual(self.bfs.bfs_adj_list(0), [0, 1])

    def test_cycle(self):
        """Test BFS on a graph with a cycle."""
        self.bfs = BFS([[1], [0, 2], [1]])
        self.assertEqual(self.bfs.bfs_adj_list(0), [0, 1, 2])

    def test_large_graph(self):
        """Test BFS on a larger graph (simulating hotel network)."""
        self.bfs = BFS([[1], [0, 2], [1, 3], [2, 4], [3]])
        self.assertEqual(self.bfs.bfs_adj_list(0), [0, 1, 2, 3, 4])

    def test_find_shortest_path(self):
        """Test BFS to find shortest path."""
        self.bfs = BFS([[1, 2], [2, 3], [0, 1, 3, 5], [1, 2, 4], [3], [2], [7], [6]])
        self.bfs.bfs_traversal(0)
        self.assertEqual(self.bfs.find_shortest_path(0, 4), [0, 1, 3, 4])
        self.assertEqual(self.bfs.find_shortest_path(0, 5), [0, 2, 5])
        self.assertEqual(self.bfs.find_shortest_path(0, 7), [])

    def test_get_distance(self):
        self.bfs = BFS([[1, 2], [2, 3], [0, 1, 3, 5], [1, 2, 4], [3], [2], [7], [6]])
        self.bfs.bfs_traversal(0)
        self.assertEqual(self.bfs.get_distance(4), 3)
        self.assertEqual(self.bfs.get_distance(5), 2)
        self.assertEqual(self.bfs.get_distance(0), 0)
        self.assertEqual(self.bfs.get_distance(2), 1)
    
    def test_count_connected_components(self):
        self.bfs = BFS([[1, 2], [0, 2], [0, 1], [4, 5], [3, 5], [3, 4]])
        self.assertEqual(self.bfs.count_connected_components(), 2)

    def test_is_it_reachable(self):
        self.bfs = BFS([[1, 2], [0, 2], [0, 1], [4, 5], [3, 5], [3, 4]])
        self.assertEqual(self.bfs.is_it_reachable(0, 2), True)
        self.assertEqual(self.bfs.is_it_reachable(0, 3), False)
        self.assertEqual(self.bfs.is_it_reachable(3, 1), False)
        self.assertEqual(self.bfs.is_it_reachable(4, 5), True)

if __name__ == "__main__":
    unittest.main()