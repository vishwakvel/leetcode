class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def backtracking(i, row, col):
            if i == len(word):
                return True
            
            if row >= m or col >= n or row < 0 or col < 0:
                return False
            
            char = board[row][col]

            if char != word[i] or char == ".":
                return False
            
            board[row][col] = "."

            found = backtracking(i+1, row, col+1) or backtracking(i+1, row, col-1) or backtracking(i+1, row+1, col) or backtracking(i+1, row-1, col)

            board[row][col] = char
            return found
        
        for r in range(m):
            for c in range(n):
                if backtracking(0, r, c):
                    return True
        
        return False
