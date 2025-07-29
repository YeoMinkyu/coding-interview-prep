from typing import Dict, List
"""
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.

Link: https://leetcode.com/problems/longest-cycle-in-a-graph/description/
"""

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        """
        Using Kosaraju’s algorithm.
        
        Time Complexity : O(|V|)
        """
        visited = set()
        stack = []

        def dfs(node):
            visited.add(node)

            neighbor = edges[node]
            if neighbor not in visited and neighbor != -1:
                dfs(neighbor)
            stack.append(node)
        
        for index in range(0, len(edges)):
            if index not in visited:
                dfs(index)

        def transpose_graph(edges) -> Dict:
            graph = {node: [] for node in range(0,len(edges))}

            for u, v in enumerate(edges):
                if v == -1:
                    continue
                graph[v].append(u)
            return graph

        transposed_graph = transpose_graph(edges)

        visited = set()
        result = -1

        def dfs_transpose(node, component):
            visited.add(node)

            for neighbor in transposed_graph[node]:
                if neighbor not in visited:
                    dfs_transpose(neighbor, component)
            component.add(node)

        while stack:
            node = stack.pop()
            component = set()

            if node not in visited:
                dfs_transpose(node, component)
                if len(component) > 1:
                    result = max(result, len(component))
            
        return result