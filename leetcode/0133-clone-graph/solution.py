"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        mapping = {}

        def dfs(n):
            if n in mapping:
                return mapping[n]
            
            copy = Node(n.val)
            mapping[n] = copy

            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
        
            return copy
        
        return dfs(node)
