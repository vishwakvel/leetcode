class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()

        def backtrack(i, r, c):
            if i >= len(word):
                return True
            
            if r >= m or c >= n or r < 0 or c < 0:
                return False
            
            if (r, c) in visited:
                return False
            
            if board[r][c] != word[i]:
                return False
            
            visited.add((r, c))
            
            
            found = backtrack(i+1, r+1, c) or backtrack(i+1, r, c+1) or backtrack(i+1, r-1, c) or backtrack(i+1, r, c-1)
            
            visited.remove((r, c))

            return found
        
        for row in range(m):
            for col in range(n):
                if backtrack(0, row, col):
                    return True
        
        return False
