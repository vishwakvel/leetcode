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
            
        queue = deque([root])
        lefttoright = True
        ans = []

        while queue:
            size = len(queue)
            level = []
            
            for i in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            if lefttoright:
                ans.append(level)
                lefttoright = False
            else:
                ans.append(level[::-1])
                lefttoright = True
        
        return ans
