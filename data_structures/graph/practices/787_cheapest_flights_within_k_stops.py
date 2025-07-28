from typing import List
from collections import deque
import heapq

"""
787. Cheapest Flights Within K Stops

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Implement using modified Bellman-Ford's algorithm

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
    
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Using Dijkstra's algorithm


        """
        if not flights:
            return -1

        graph = {node: [] for node in range(0, n)}

        for u, v, w in flights:
            graph[u].append((v, w))

        visited = {} # key: (node, stops), value: cost

        pq = [(0, src, 0)] # cost, src, stops

        while pq:
            cost, node, stops = heapq.heappop(pq)

            if node == dst: # minimum cost at most k times visited cities
                return cost

            state = (node, stops)
            if state in visited and visited[(node, stops)] <= cost: 
                continue

            if stops >= k+1: # if stops already exceed k times, skip the check neighbor nodes.
                continue

            visited[(node, stops)] = cost

            for neighbor, weight in graph[node]:
                neighbor_cost = cost + weight
                neighbor_stops = stops + 1
                heapq.heappush(pq, (neighbor_cost, neighbor, neighbor_stops))
        
        return -1
            

            

        """
        Using Dijkstra but time exceeded
        """
        # if not flights:
        #     return -1

        # graph = {node: [] for node in range(0, n)}

        # for u, v, w in flights:
        #     graph[u].append((v, w))

        # distance = {node: float('inf') for node in range(0, n)}
        # stops = {node: float('inf') for node in range(0, n)}
        # pq = [(0, src, 0)]
        # distance[src] = 0
        # stops[src] = 0


        # while pq:
        #     current_distance, node, current_stops = heapq.heappop(pq)

        #     if node == dst:
        #         return current_distance
        #     if current_stops == k+1:
        #         continue
            
        #     for neighbor, weight in graph[node]:
        #         neighbor_distance = current_distance + weight
        #         neighbor_stops = current_stops + 1

        #         if neighbor_distance < distance[neighbor]:
        #             distance[neighbor] = neighbor_distance
        #             stops[neighbor] = neighbor_stops
        #         elif neighbor_stops < stops[neighbor]:
        #             stops[neighbor] = neighbor_stops

        #         heapq.heappush(pq, (neighbor_distance, neighbor, neighbor_stops))

        # return -1

class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Using BFS
        """
        graph = {node: [] for node in range(0, n)}
        for u, v, w in flights:
            graph[u].append((v, w))

        queue = deque([(0, src, 0)])
        distance = [float('inf')]*n
        # visited = {}

        distance[src] = 0

        while queue:
            cost, node, stops = queue.popleft()
            if stops >= k + 1:
                continue

            state = (node, stops)

            for neighbor, weight in graph[node]:
                if distance[neighbor] > cost + weight:
                    distance[neighbor] = cost + weight
                    queue.append((distance[neighbor], neighbor, stops + 1))

        return distance[dst] if distance[dst] != float('inf') else -1