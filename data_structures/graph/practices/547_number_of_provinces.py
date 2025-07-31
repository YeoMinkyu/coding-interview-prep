from collections import deque
from typing import List

"""
547. Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Link: https://leetcode.com/problems/number-of-provinces/description/
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        provinces = 0

        for node in range(0, len(isConnected)):
            if node not in visited:
                provinces += 1
                queue.append(node)

            while queue:
                node = queue.popleft()
                visited.add(node)

                for neighbor, connected in enumerate(isConnected[node]):
                    if neighbor not in visited and connected == 1:
                        queue.append(neighbor)

        return provinces