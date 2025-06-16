from collections import deque

def bfs_adj_list(graph: list[list[int]], start: int) -> list[int]:
    """
    Perform BFS on a graph represented as an adjacency list, returning visited nodes in order.
    Time: O(V + E), where V is the number of vertices and E is the number of edges.
    Space: O(V) for the queue and visited array.
    Example:
        Input: graph = [[1, 2], [0, 3], [0], [1]], start = 0 -> Output: [0, 1, 2, 3]
    Edge Cases:
        - Empty graph or invalid start node: return []
        - Disconnected graph: visits all reachable nodes
        - Cycle: handles without infinite loop
    Hint: Use a queue to explore nodes level by level, marking visited nodes.
    """

    if not graph or start < 0 or start >= len(graph):
        return []
    
    queue = deque()
    visited_vertices = set()
    output = []

    queue.append(start)
    visited_vertices.add(start)

    while queue:
        current_vertex = queue.popleft()
        output.append(current_vertex)

        for edge in graph[current_vertex]:
            if edge not in visited_vertices:
                queue.append(edge)
                visited_vertices.add(edge)
    
    return output


"""
TBD

Interviewer Feedback and Follow-Up
Interviewer: "This test suite covers the core requirements well. Once you’ve implemented bfs_adj_list and run the tests, let me know the results. Here’s a follow-up question to prepare for:

Question: 'How would you modify bfs_adj_list to return the shortest path length from start to each node instead of the visitation order?'
Hint: Use a distance array initialized with infinity, updating it as you enqueue nodes.
Expected Response: Explain using a dist array, setting dist[start] = 0, and incrementing distance for each level.
Please implement and test now. You have 10 minutes remaining. If you need clarification or additional test cases, feel free to ask!"
"""
