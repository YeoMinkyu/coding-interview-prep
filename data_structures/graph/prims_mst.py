from typing import Dict, List, Tuple
import heapq

def prims_mst(graph: Dict[int, List[Tuple[int, int]]]) -> List[Tuple[int, int, int]]:
    """
    Find a minimum spanning tree using Prim's algorithm

    Args:
        graph (dict): A dictionary of an undirected graph with nodes(int) and the list of edges with weight for each edge

    Returns:
        list: The list of a minimum spanning tree (u, v, weight)

    Time Complexity: O((V+E)logV)
    Space Complexity: O(V)
    """
    
    if not graph:
        return []
    
    nodes_with_edges = [node for node in graph if len(graph[node]) > 0]

    if len(nodes_with_edges) == 0:
        return []

    visited = set()
    mst = []

    priority_queue = [(0, nodes_with_edges[0] , None)] # weight, node, parent

    while priority_queue and len(visited) < len(nodes_with_edges):
        weight, node, parent = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        if parent != None:
            if node < parent:
                mst.append((node, parent, weight))
            else:
                mst.append((parent, node, weight))

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (weight, neighbor, node))

    return mst