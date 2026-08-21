from collections import defaultdict

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        indexes = {}
        rows = [0] * len(mat)
        cols = [0] * len(mat[0])

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                indexes[mat[r][c]] = (r, c)
        
        for i in range(len(arr)):
            row, col = indexes[arr[i]]
            rows[row] += 1
            cols[col] += 1

            if rows[row] == len(mat[0]) or cols[col] == len(mat):
                return i
