class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m = len(grid)
        n = len(grid[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"

            for dr, dc in dirs:
                dfs(row + dr, col + dc)
        
        islands = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        
        return islands
