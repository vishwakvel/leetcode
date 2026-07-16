"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        hmap = {} # old to new node
        curr = head
        
        while curr:
            node = Node(curr.val, curr.next, curr.random)
            hmap[curr] = node
            curr = curr.next
        
        curr = head

        while curr:
            hmap[curr].next = hmap.get(curr.next)
            hmap[curr].random = hmap.get(curr.random)
            curr = curr.next
        
        return hmap[head]
