from typing import List, Set, Tuple

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int, total: int, visited: Set[Tuple[int, int]]) -> int:
            # Out of bounds or blocked or already visited
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] == 1 or 
                (r, c) in visited):
                return 0

            # Reached target
            if r == rows - 1 and c == cols - 1:
                return 1

            # Mark current as visited
            visited.add((r, c))

            # Explore neighbors
            total += dfs(r + 1, c, 0, visited)
            total += dfs(r - 1, c, 0, visited)
            total += dfs(r, c + 1, 0, visited)
            total += dfs(r, c - 1, 0, visited)

            # Backtrack
            visited.remove((r, c))

            return total

        return dfs(0, 0, 0, set())
