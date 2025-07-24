"""
743. Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Link: https://leetcode.com/problems/network-delay-time/description/
"""
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if not times:
            return -1

        graph = {u: [] for u, v, w in times}

        for u, v, w in times:
            graph[u].append((w, v))

        print(graph)
        distance = {k: 0}
        priority_queue = [(0, k)]
        visited = set()

        while priority_queue:
            current_distance, node = heapq.heappop(priority_queue)

            visited.add(node)

            for weight, v in graph.get(node, []):
                if v not in visited:
                    if v not in distance or distance[v] > current_distance + weight:
                        distance[v] = current_distance + weight
                        heapq.heappush(priority_queue,(distance[v], v))

        if not distance or len(distance) != n:
            return -1
        else:
            return max(distance.values())

