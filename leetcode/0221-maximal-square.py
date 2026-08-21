class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        biggest = {}
        ans = 0

        def dp(row, col):
            nonlocal ans

            if row >= rows or col >= cols:
                return 0
            
            if (row, col) in biggest:
                return biggest[(row, col)]
            
            if matrix[row][col] == "0":
                biggest[(row, col)] = 0
                return 0
            
            biggest[(row, col)] = 1 + min(dp(row, col + 1), dp(row + 1, col), dp(row + 1, col + 1))

            ans = max(ans, biggest[(row, col)])
            return biggest[(row, col)]
        
        for r in range(rows):
            for c in range(cols):
                dp(r, c)
            
        return ans * ans
