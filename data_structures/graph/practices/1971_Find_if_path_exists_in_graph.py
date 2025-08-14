from collections import defaultdict
from typing import *

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Using Iteratvie Approach
        Time: Complexity: O(V+E)
        Space Complexity: O(V+E)
        """
        if source == destination:
            return True

        graph = defaultdict(list)
        stack = [source]
        visited = {source}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        while stack:
            node = stack.pop()
            
            for neighbor in graph[node]:
                if neighbor == destination:
                    return True
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
                    

        return False

        """
        Using Recursive DFS
        Time Complexity: O(|V| + |E|)
        Space Complexity: O(|V|)
        """
        
        if source == destination:
            return True

        graph = defaultdict(list)
        visited = set()

        for u, v in edges: # edge: the pairs of (u, v)
            graph[u].append(v) # (u, v)
            graph[v].append(u) # (v, u)

        def dfs(node: int) -> bool:
            if node == destination:
                return True
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited and dfs(neighbor):
                    return True
            return False
            
        return dfs(source)