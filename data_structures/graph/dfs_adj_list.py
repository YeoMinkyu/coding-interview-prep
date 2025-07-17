def dfs_recursive(graph: {int, list[int]}, start: int) -> list[int]:

    if not graph or start not in graph:
        return []

    visited = {}
    parents = {}
    result = []

    def dfs(node):
        visited[node] = True
        result.append(node)

        for neighbor in graph[node]:
            if not visited.get(neighbor, False):
                parents[neighbor] = node
                dfs(neighbor)
    
    dfs(start)

    return result

def dfs_iterative(graph: {int, list[int]}, start: int) -> list[int]:
    if not graph or start not in graph:
        return []

    dfs_stack = []
    visited = {}
    parents = {}
    result = []

    dfs_stack.append(start)
    visited[start] = True
    parents[start] = None
    result.append(start)

    while dfs_stack:

        for neighbor in graph[dfs_stack[-1]]:
            if not visited.get(neighbor, False):
                visited[neighbor] = True
                parents[neighbor] = dfs_stack[-1]
                dfs_stack.append(neighbor)
                result.append(neighbor)
                break
        else:
            dfs_stack.pop()

        # current_node = dfs_stack.pop()
        # result.append(current_node)
        
        # for neighbor in reversed(graph[current_node]):
        #     if not visited.get(neighbor, False):
        #         visited[neighbor] = True
        #         parents[neighbor] = current_node
        #         dfs_stack.append(neighbor)

    return result

def has_cycle(graph: {int, list[int]}, start: int) -> bool:
    """
    Check the graph has cycle

    Args:
        graph (dict) : A dictionary has verticies and adjacency list of the vertext
        start (int) : Starting node
    
    Returns:
        bool : True if the graph has cycle, otherwise False
    """

    if not graph or start not in graph:
        return False

    # 0 (White): Not visited yet
    # 1 (Gray) : Being processing
    # 2 (Black) : Finished 
    colors = {node: 0 for node in graph}

    stack = [(start, 0, None)] # node, neighbor_index, parent
    colors[start] = 1

    while stack:

        node, neighbor_index, parent = stack[-1]

        if neighbor_index >= len(graph[node]): # Visited all neighbors of the current node
            colors[node] = 2
            stack.pop()
            continue
            
        neighbor = graph[node][neighbor_index]
        stack[-1] = (node, neighbor_index+1, parent)

        # Skip the parent node(Visited right before)
        if neighbor == parent:
            continue

        if colors[neighbor] == 1:
            return True

        if colors[neighbor] == 0:
            stack.append((neighbor, 0, node))
            colors[neighbor] = 1       

    return False
