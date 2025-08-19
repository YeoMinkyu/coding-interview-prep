from heapq import *
from collections import *
from typing import *

"""

"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        #1 Approach using BFS

        Time Complexity: O(N), Each of the N cells is processed at most once

        Space Complexity: O(N), The visited set requires O(N) space, in the worst case, it will hold the row and colum of each of the N cells.

        """
        n = len(grid[0])
        max_row = n - 1
        max_col = n - 1
        adjacent_cell = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] # 8 direction from the current position

        def get_neighbors(row, col):
            for x, y in adjacent_cell:
                coord_x = row + x
                coord_y = col + y
                if not(0 <= coord_x <= max_row and 0 <= coord_y <= max_col):
                    continue
                if grid[coord_x][coord_y] != 0:
                    continue
                yield (coord_x, coord_y)
        

        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        if n == 1:
            return 1

        queue = deque([(0, 0)]) # row, col


        distance = 1
        visited = defaultdict()
        visited = {(0, 0)}

        while queue:
            num_of_neighbors = len(queue)
            
            for _ in range(num_of_neighbors):
                i, j = queue.popleft()

                for coord_x, coord_y in get_neighbors(i, j):
                    if coord_x == max_row and coord_y == max_col:
                        return distance + 1
                    if (coord_x, coord_y) not in visited:
                        visited.add((coord_x, coord_y))
                        queue.append((coord_x, coord_y))

            distance += 1

        return -1

        """
        #2 Approach using min heap
        """
        # n = len(grid[0])

        # if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        #     return -1
        
        # if n == 1:
        #     return 1

        # adjacent_cell = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] # 8
        # queue = [(1, 0, 0)]
        # distance = [[float('inf')]*n for _ in range(n)]
        # visited = set()

        # distance[0][0] = 1

        # while queue:
        #     length, i, j = heappop(queue)

        #     if i == n-1 and j == n-1:
        #         return length

        #     visited.add((length, i, j))

        #     for x, y in adjacent_cell:
        #         coord_x = i + x
        #         coord_y = j + y
        #         if 0 <= coord_x <= n-1 and 0 <= coord_y <= n-1 and grid[coord_x][coord_y] == 0:
        #             if distance[coord_x][coord_y] > length+1 and (length+1, coord_x, coord_y) not in visited:
        #                 distance[coord_x][coord_y] = length + 1
        #                 heappush(queue, (length+1, coord_x, coord_y))

        # return -1