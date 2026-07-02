class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            
            if grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0
            area = 1

            for dr, dc in dirs:
                area += dfs(r + dr, c + dc)
            
            return area
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))
        
        return max_area
