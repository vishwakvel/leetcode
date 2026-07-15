# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = deque([root])
        lefttoright = True

        while q:
            size = len(q)
            level = []
            
            for i in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            if lefttoright:
                ans.append(level)
                lefttoright = not lefttoright 
            else:
                ans.append(level[::-1])
                lefttoright = not lefttoright
        
        return ans
