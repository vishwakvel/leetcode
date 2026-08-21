from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        minutes = 0
        queue = deque()
        fresh = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue and fresh > 0:
            size = len(queue)

            for i in range(size):
                r, c = queue.popleft()

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
                    
            minutes += 1
        
        return minutes if not fresh else -1
