class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        def backtracking(index, row, col):
            if index == len(word):
                return True

            if row < 0 or col < 0 or row >= m or col >= n:
                return False

            char = board[row][col]

            if char != word[index] or char == ".":
                return False
            
            board[row][col] = "."

            found = backtracking(index+1, row+1, col) or backtracking(index+1, row-1, col) or backtracking(index+1, row, col+1) or backtracking(index+1, row, col-1)

            board[row][col] = char
            return found
        
        for r in range(m):
            for c in range(n):
                if backtracking(0, r, c):
                    return True
        
        return False
