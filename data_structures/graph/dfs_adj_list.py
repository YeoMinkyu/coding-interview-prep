from typing import Dict, List, Set

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
        graph (dict) : A dictionary has verticies and adjacency list of the vertex
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

def count_connected_components(graph: {int, list[int]}) -> int:
    """
    Count the number of connected components on a graph

    Args:
        graph (dict) : A dictionary has vertices and adjacency list of the vertex

    Return:
        int : The number of conntected components

    Time Complexity : O(|V| * (|V| + |E|)
    Space Complexity : O(|V|)
    """
    if not graph:
        return 0
    
    count = 0
    visited = set()

    def dfs(node: int) -> None:
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in graph:
        if node not in visited:
            count += 1
            dfs(node)

    return count

def count_connected_components_iteration(graph: {int, list[int]}) -> int:
    if not graph:
        return 0
    
    count = 0
    visited = set()

    for node in graph:
        if node in visited:
            continue
        
        count += 1
        stack = [(node, 0)] # node, neighbor_index
        visited.add(node)

        while stack:
            node, neighbor_index = stack[-1]

            if neighbor_index >= len(graph[node]):
                stack.pop()
                continue

            neighbor = graph[node][neighbor_index]
            stack[-1] = (node, neighbor_index + 1)

            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, 0))

    return count

def find_scc(graph: Dict[int, List[int]]) -> List[Set[int]]:
    """
    Args:
        graph (dict): A dictionary has vertecies and an ajacency list of the vertex
        example: graph = {0: [1], 1: [2], 2: [0, 3], 3: [4], 4: [3]}
    
    Returns:
        List : List of SCCs

    Time complexity : O(|V|+|E|)
    
    """
    if not graph:
        return []
    
    visited = set()
    stack = []

    def dfs(node: int) -> None:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    def transpose_graph(graph: Dict[int, List[int]]) -> Dict[int, List[int]]:
        # example: graph = {0: [1], 1: [2], 2: [0, 3], 3: [4], 4: [3]}
        all_nodes = set(graph.keys())
        for neighbors in graph.values():
            all_nodes.update(neighbors)
        transposed_graph = {node: [] for node in all_nodes}
        
        for node in graph:
            for neighbor in graph[node]:
                transposed_graph[neighbor].append(node)
        for node in transposed_graph:
            transposed_graph[node].sort()

        return transposed_graph
    

    transposed_graph = transpose_graph(graph)

    def dfs_transpose(node: int, component: Set[int]) -> None:
        visited.add(node)
        component.add(node)

        for neighbor in transposed_graph[node]:
            if neighbor not in visited:
                dfs_transpose(neighbor, component)
    
    visited = set()
    sccs = []

    while stack:
        node = stack.pop()
        
        if node not in visited:
            component = set()
            dfs_transpose(node, component) # Why component shoud be an argument for this function? To check clearly
            sccs.append(component)
    
    return sccs

def is_bipartite(graph: Dict[int, List[int]]) -> bool:
    """
    Check if graph is bipartite using recursive DFS with sigle-pass coloring.

    A graph is bipartite if its vertices can be colored with 2 colors such that no two adjacency vertices have the same color.

    Args:
        graph (Dict) : Dictionary mapping each vertex to its adjacency list

    Returns:
        bool : True if graph is bipartite, False otherwise

    Time Complexity: O(|V| + |E|)
    Space Complexity: O(|V|)
    """
    if not graph:
        return True

    # To check for self-loops(makes graph non-bipartite)
    for node, neighbors in graph.items():
        if node in neighbors:
            return False

    visited = set()
    colors = dict()

    def dfs_coloring(node: int) -> bool:
        """
        Color the node and recursively check/color its neighbors.
        
        Args:
            node: Current node to color
            color: Color to assign to current node
            
        Returns:
            True if coloring is valid (no conflicts), False otherwise
        """
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                colors[neighbor] = -colors[node]
                if not dfs_coloring(neighbor):
                    return False
            elif colors[neighbor] == colors[node]:
                return False
        return True
            

    for node in graph:
        if node not in visited:
            colors[node] = 1
            if not dfs_coloring(node):
                return False
    return True
