class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n:
                return
            
            if grid[row][col] == "0":
                return
            
            grid[row][col] = "0" # was island now change to 0 to mark visited
            
            for dr, dc in dirs:
                nr = dr+row
                nc = dc+col
                dfs(nr, nc)
        
        islands = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        
        return islands
