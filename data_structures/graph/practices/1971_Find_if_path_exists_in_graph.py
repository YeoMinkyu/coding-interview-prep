from collections import defaultdict
from typing import *

"""
1971. Find if Path Exists in Graph

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 

Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:


Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.

Link: https://leetcode.com/problems/find-if-path-exists-in-graph/description/
"""

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Using Union and Find Approach
        Time Complexity: O(α(N), O(N) when creating two arrays for Union and Find.
        Space Complexity: O(N) 
        """
        root = {i: i for i in range(n)}
        height = {i: 1 for i in range(n)}

        def find(node: int) -> int:
            if node == root[node]:
                return node

            root[node] = find(root[node])
            return root[node]
        
        def union(u: int, v: int) -> None:
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                if height[root_u] > height[root_v]:
                    root[root_v] = root_u
                elif height[root_v] > height[root_u]:
                    root[root_u] = root_v
                else:
                    root[root_v] = root_u
                    height[root_u] += 1

        def connected(u: int, v: int) -> bool:
            return find(u) == find(v)

        for u, v in edges:
            union(u, v)

        return connected(source, destination)

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