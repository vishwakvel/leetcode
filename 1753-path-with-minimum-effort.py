import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0, 0, 0)]
        rows = len(heights)
        cols = len(heights[0])
        effort = [[float("inf")] * cols for i in range(rows)]
        effort[0][0] = 0
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while heap:
            e, r, c = heapq.heappop(heap)
            
            if r == rows-1 and c == cols-1:
                return e

            if e > effort[r][c]:
                continue
            
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    diff = abs(heights[r][c] - heights[nr][nc])
                    new = max(e, diff)

                    if new < effort[nr][nc]:
                        effort[nr][nc] = new
                        heapq.heappush(heap, (new, nr, nc))
        
        return 0
