from typing import List, Set, Tuple
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        def bfs(start: Tuple[int, int]) -> int:
            
            q = deque([(0, 0, 0)]) # (row, col, count)
            visited = set()
            visited.add((0, 0))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q: 

                r, c, count = q.popleft()

                if (r, c) == (rows - 1, cols - 1):
                    return count

                for dr, dc in directions: 
                    rn, cn = r + dr, c + dc

                    if (0 <= rn < rows and 0 <= cn < cols and (rn, cn) not in visited and grid[rn][cn] == 0):

                        visited.add((rn, cn))

                        q.append((rn, cn, count + 1))
            return -1

        return bfs((0, 0))
