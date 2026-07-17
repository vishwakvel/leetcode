class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, -1), (-1, 0), (1, 0), (0, 1)]

        def dfs(r, c):
            if r >= m or c >= n or r < 0 or c < 0 or grid[r][c] == "0":
                return False
            
            grid[r][c] = "0"

            for dr, dc in dirs:
                dfs(r+dr, c+dc)
        
        islands = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1
        
        return islands
