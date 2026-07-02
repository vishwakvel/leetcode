class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            if grid[r][c] != '1':
                return
            
            grid[r][c] = '#'

            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        
        islands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(row, col)
        
        return islands
