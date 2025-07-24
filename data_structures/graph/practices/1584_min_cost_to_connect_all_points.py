"""
1584. Min Cost to Connect All Points

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Link: https://leetcode.com/problems/min-cost-to-connect-all-points/description/
"""

import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        {0: [(1, 4), (2, 13), (3, 7), (4, 7)], 1: [(0, 4), (2, 9), (3, 3), (4, 7)], 2: [(0, 13), (1, 9), (3, 10), (4, 14)], 3: [(0, 7), (1, 3), (2, 10), (4, 4)], 4: [(0, 7), (1, 7), (2, 14), (3, 4)]}
        """
        graph = {node: [] for node in range(0, len(points))}
        
        # graph = {node: [(v, weight)]}
        for u in range(0, len(points)-1):
            for v in range(u+1, len(points)):
                graph[u].append((v, abs((points[u][0] - points[v][0])) + abs((points[u][1]-points[v][1]))))
                graph[v].append((u, abs((points[u][0] - points[v][0])) + abs((points[u][1]-points[v][1]))))


        visited = set()
        distance = 0
        priority_queue = [(0, 0)]

        while priority_queue or len(visited) < len(points):
            current_weight, node = heapq.heappop(priority_queue)

            if node in visited:
                continue

            visited.add(node)

            distance += current_weight

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (weight, neighbor))


        return distance
