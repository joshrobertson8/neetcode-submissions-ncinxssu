class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c, i, visited):
            if i == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if (r, c) in visited:
                return False

            if board[r][c] != word[i]:
                return False

            visited.add((r, c))

            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1, visited):
                    return True

            visited.remove((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0, set()):
                    return True

        return False