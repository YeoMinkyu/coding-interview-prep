from typing import List, Dict
"""
210. Course Schedule II (Medium)

Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]

Link: https://leetcode.com/problems/course-schedule-ii/description/
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]

        answer = []
        visited = set()
        graph = {node: [] for node in range(0, numCourses)}

        for v, u in prerequisites:
            if v == u:
                return answer

            graph[v].append(u)

        if self.has_cycle(graph):
            return answer

        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            answer.append(node)

        for node in graph:
            if node not in visited:
                dfs(node)

        return answer

    def has_cycle(self, graph: Dict[int, List[int]]) -> bool:
        WHITE, GRAY, BLACK = 0, 1, 2

        colors = {node: WHITE for node in graph}
        stack = [] # node, neighbor_index

        for node in graph:
            if colors[node] != WHITE:
                continue

            stack.append((node, 0))
            colors[node] = GRAY

            while stack:
                node, neighbor_index = stack[-1]

                if neighbor_index >= len(graph[node]):
                    colors[node] = BLACK
                    stack.pop()
                    continue

                neighbor = graph[node][neighbor_index]
                stack[-1] = (node, neighbor_index + 1)

                if colors[neighbor] == BLACK:
                    continue

                if colors[neighbor] == GRAY:
                    return True
                
                if colors[neighbor] == WHITE:
                    stack.append((neighbor, 0))
                    colors[neighbor] = GRAY

        return False
                