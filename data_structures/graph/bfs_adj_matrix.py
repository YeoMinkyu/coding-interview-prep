from collections import deque

def bfs_adj_matrix(graph: list[list[int]], start: int) -> list[int]:
    """
    Perform BFS on a graph represented as an adjacency matrix, returning visited nodes in order.
    Time: O(V^2), where V is the number of vertices.
    Space: O(V) for the queue and visited array.
    Example:
        Input: graph = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]], start = 0 -> Output: [0, 1, 2, 3]
    Edge Cases:
        - Empty graph or invalid start node: return []
        - Disconnected graph: visits all reachable nodes
        - Cycle: handles without infinite loop
    Hint: Use a queue to explore nodes, checking matrix rows for neighbors.
    """
    if not graph or start < 0 or start >= len(graph):
        return []
    
    visited = set()
    output = []
    queue = deque()

    queue.append(start)
    visited.add(start)

    while queue:
        current_vertex = queue.popleft()
        output.append(current_vertex)
       
        for neighbor, edge in enumerate(graph[current_vertex]):
            if edge == 1 and neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return output