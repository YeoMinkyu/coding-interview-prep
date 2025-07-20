from collections import deque

class BFS:
    def __init__(self, graph: list[list[int]]= None):
        self._graph = graph if graph is not None else []
        self.queue = deque()
        self.visited_vertices = dict()
        self.parents = []
        self.bfs_result = []

    def bfs_traversal(self, start: int) -> None:
        """
        Traverse the graph using BFS from the given start node.

        Args:
            start (int): The starting node for BFS
        Side effects:
            Updates self.visited_vertices, self.parents, and self.bfs_result with traversal state.

        Time: O(V + E), where V is the number of vertices and E is the number of edges.
        Space: O(V) for the queue and visited array.
        """

        if not self._graph or start < 0 or start >= len(self._graph):
                return []

        self.queue.clear()
        self.visited_vertices.clear()
        self.parents = [None] * len(self._graph)
        self.bfs_result = []

        self.queue.append(start)
        self.visited_vertices[start] = 0 # check whether the edge is visited and save distance from the start
        self.parents[start] = None

        while self.queue:
            current_vertex = self.queue.popleft()
            self.bfs_result.append(current_vertex)

            for edge in self._graph[current_vertex]:
                if edge not in self.visited_vertices:
                    self.queue.append(edge)
                    self.parents[edge] = current_vertex
                    self.visited_vertices[edge] = self.visited_vertices[self.parents[edge]] + 1

    def bfs_adj_list(self, start: int) -> list[int]:
        """
        Perform BFS traversal from the given start node and return the visitation order.

        Args:
            start(int): The starting node.

        Returns:
            List[int]: Nodes visited in BFS order from the start node. 

        Notes:
            - Empty graph or invalid start node: return [].
            - Visits only nodes reachable from the start node.
            - Handles disconnected graphs and cycles safely.
        """
        self.bfs_traversal(start)

        return self.bfs_result
    
    def get_distance(self, end: int) -> int:
        """
        Return the shortest distance from the start node to `end`, after BFS traversal.
        
        Args:
            end (int): Target node.

        Returns:
            int: Number of edges from start to `end`, or float('inf') if unreachable.
        """

        return self.visited_vertices.get(end, float('inf'))

    def find_shortest_path(self, start: int, end: int) -> list[int]:
        """
        Return the shortest path from `start` to `end` as a list of nodes, after BFS traversal.

        Args:
            start (int): Starting node.
            end (int): Target node.

        Returns:
            List[int]: List of nodes representing the shortest path, or [] if unreachable.
        """

        # Iterative Ver.

        path = []

        if end not in self.visited_vertices:
            return path

        current = end
        
        while current != None:
            
            path.append(current)
            current = self.parents[current]
        
        path.reverse()

        return path if path[0] == start else []

        
        """
        Recursive Ver.
            if shortest_path is None:
                    shortest_path = []
                
                if end not in self.visited_vertices or self.parents[end] is None:
                    if start != end:
                        return []
                    else: 
                        shortest_path.append(start)
                        return shortest_path
                
                shortest_path = self.find_shortest_path(start, self.parents[end], shortest_path)
                shortest_path.append(end)

                return shortest_path
        """

    def count_connected_components(self) -> int:
        """
        Count the number of connected components in the graph.
        
        Returns:
            int: The number of connected components.
        
        """
        count = 0
        visited = {}

        for vertex in range(len(self._graph)):
            if vertex not in visited:
                count += 1
                self.bfs_traversal(vertex)
                visited.update(self.visited_vertices)

        return count
    
    def is_it_reachable(self, start: int, end: int) -> bool:
        """
        Return True if `end` is reachable from `start` using BFS; otherwise, return False.

        Args:
            start (int): starting node.
            end (int): Target node.

        Returns:
            bool: True if `end` is reachable from `start`, otherwise False.
        """

        self.bfs_traversal(start)

        if end in self.visited_vertices:
            return True
        else:
            return False