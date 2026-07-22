class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        maxarea = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            area = 1

            for nr, nc in dirs:
                area += dfs(row + nr, col + nc)

            return area
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                   maxarea = max(maxarea, dfs(r, c))
        
        return maxarea
