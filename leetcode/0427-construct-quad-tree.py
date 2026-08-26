"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dac(row, col, size):
            value = grid[row][col]
            same = True

            for i in range(row, row + size):
                for j in range(col, col + size):
                    if grid[i][j] != value:
                        same = False
                        break
                
                if not same:
                    break
            
            if same:
                return Node(value==1, True, None, None, None, None)
            
            half = size // 2

            topLeft = dac(row, col, half)
            topRight = dac(row, col + half, half)
            bottomLeft = dac(row + half, col, half)
            bottomRight = dac(row + half, col + half, half)

            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return dac(0, 0, len(grid))