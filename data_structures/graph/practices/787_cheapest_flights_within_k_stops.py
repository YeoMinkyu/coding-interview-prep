from typing import List

"""
787. Cheapest Flights Within K Stops

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Time complexity: O(k*|E|)
        """
        if not flights:
            return -1

        distance = {node: float('inf') for node in range(0, n)}
        distance_temp = {node: float('inf') for node in range(0, n)}

        distance[src] = 0
        distance_temp[src] = 0

        for _ in range(0, k+1):
            for u, v, w in flights:
                if distance[u] != float('inf') and distance_temp[v] > distance[u] + w:
                    distance_temp[v] = distance[u] + w

            for node, weight in distance_temp.items():
                distance[node] = weight

        
        return distance[dst] if distance[dst] != float('inf') else -1