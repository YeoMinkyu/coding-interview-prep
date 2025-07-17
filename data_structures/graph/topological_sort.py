def topological_sort(graph: dict[int, list[int]]) -> list[int]:
        """
        Performs topological sorting on the input directed acyclic graph (DAG).

        Args:
            graph (dict[int, list[int]]): Adjacency list representing the DAG.

        Returns:
            list[int]: A list of vertices in topologically sorted order.
        """
        
        visited = {}
        ordered_result = []

        def dfs(node):
            visited[node] = True

            for neighbor in graph[node]:
                if not visited.get(neighbor, False):
                    dfs(neighbor)
            
            ordered_result.append(node)

        if has_cycle(graph):
            return ordered_result 

        for node in graph:
            if not visited.get(node, False):
                dfs(node)

        ordered_result.reverse()

        return ordered_result

def has_cycle(graph: dict[int, list[int]]) -> bool:
    if not graph:
        return False

    WHITE, GRAY, BLACK = 0, 1, 2
    colors = {vertex: WHITE for vertex in graph}   
    
    for node in graph:
        if colors[node] != WHITE:
            continue

        stack = [(node, 0)] # node, neighbor_index
        colors[node] = GRAY

        while stack:
            node, neighbor_index = stack[-1]

            if neighbor_index >= len(graph[node]):
                colors[node] = BLACK
                stack.pop()
                continue

            stack[-1] = (node, neighbor_index + 1)
            neighbor = graph[node][neighbor_index]

            if colors[neighbor] == BLACK:
                continue

            if colors[neighbor] == GRAY:
                return True
            
            if colors[neighbor] == WHITE:
                colors[neighbor] = GRAY
                stack.append((neighbor, 0))
                continue

    return False