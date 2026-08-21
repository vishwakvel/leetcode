class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        r = 0
        c = n-1

        while 0 <= r < m and 0 <= c < n:
            curr = matrix[r][c]
            
            if curr == target:
                return True
            
            if curr > target:
                c -= 1
            
            if curr < target:
                r += 1
