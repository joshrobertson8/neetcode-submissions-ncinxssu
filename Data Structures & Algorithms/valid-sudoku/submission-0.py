class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Each row must contain the digits 1-9 without duplicates.
        # Each column must contain the digits 1-9 without duplicates.
        # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)


        for r in range(9): 
            for c in range(9):

                if board[r][c] == ".": 
                    continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]: 
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True