from collections import deque
from typing import List
"""
886. Possible Bipartition

We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: The first group has [1,4], and the second group has [2,3].
Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.

Link: https://leetcode.com/problems/possible-bipartition/description/
"""

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True

        graph = {node: [] for node in range(0, n)}
        for u, v in dislikes:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)

        queue = deque()
        visited = set()
        colors = [None]*n

        for node in range(0, n):
            if node not in visited:
                queue.append(node)
                colors[node] = 1

                while queue:
                    node = queue.popleft()

                    visited.add(node)

                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            colors[neighbor] = -colors[node]
                        elif colors[neighbor] == colors[node]:
                            return False
        return True


