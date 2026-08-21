from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        queue = deque()

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else: # set 1s as unvisited
                    mat[r][c] = -1
        
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while queue:
            row, col = queue.popleft()

            for dr, dc in dirs:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[row][col] + 1
                    queue.append((nr, nc))

        return mat
