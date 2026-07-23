from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        queue = deque([(sr, sc)])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ogcolor = image[sr][sc]

        if ogcolor == color:
            return image
        
        image[sr][sc] = color

        while queue:
            row, col = queue.popleft()

            for nr, nc in dirs:
                dr = row + nr
                dc = col + nc

                if 0 <= dr < m and 0 <= dc < n and image[dr][dc] == ogcolor:
                    image[dr][dc] = color
                    queue.append((dr, dc))
        
        return image
