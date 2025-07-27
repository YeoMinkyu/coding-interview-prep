def bellman_ford(edges: list[tuple[int, int, int]], num_vertices: int, source: int) -> tuple[dict[int, int], bool]:
    if not edges and num_vertices <= 0 or source >= num_vertices:
        return ({}, False)

    if num_vertices == 1:
        return {source: 0}, False
    
    has_negative_cycle = False


    distance = {node: float('inf') for node in range(0, num_vertices)}

    distance[source] = 0

    for _ in range(0, num_vertices-1):
        updated = False
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                updated = True
        
        if not updated:
            break

    for u, v, w in edges:
        if distance[u] != float('inf') and distance[v] > distance[u] + w:
            has_negative_cycle = True
            break

    return (distance, has_negative_cycle)