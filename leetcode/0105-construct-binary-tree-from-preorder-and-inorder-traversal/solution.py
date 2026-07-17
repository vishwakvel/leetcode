# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {val: i for i, val in enumerate(inorder)}
        p = 0

        def dfs(left, right):
            nonlocal p

            if left > right:
                return None
            
            nodeval = preorder[p]
            p += 1

            node = TreeNode(nodeval)
            index = hashmap[nodeval]

            node.left = dfs(left, index-1)
            node.right = dfs(index+1, right)

            return node
        
        return dfs(0, len(inorder) - 1)
