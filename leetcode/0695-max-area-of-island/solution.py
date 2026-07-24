class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            area = 1

            for dr, dc in dirs:
                nr = row + dr
                nc = col + dc

                area += dfs(nr, nc)
            
            return area
        
        maxarea = 0
        
        for r in range(m):
            for c in range(n):
                maxarea = max(maxarea, dfs(r, c))
        
        return maxarea
