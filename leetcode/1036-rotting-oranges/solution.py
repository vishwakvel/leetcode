class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        minutes = 0

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in dirs:
                    nr = dr + r
                    nc = dc + c
                
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            
            minutes += 1
        
        return minutes if fresh == 0 else -1
