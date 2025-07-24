from typing import Dict, List, Tuple
import heapq

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], source: int) -> Dict[int, int]:
    if not graph or source not in graph:
        return {}

    distance = {source: 0}
    priority_queue = [(0, source)]
    visited = set()

    while priority_queue:
        current_distance, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                if neighbor not in distance or distance[neighbor] > current_distance + weight:
                    distance[neighbor] = current_distance + weight
                    heapq.heappush(priority_queue, (distance[neighbor], neighbor))

    for node in graph:
        if node not in distance:
            distance[node] = float('inf')

    return distance