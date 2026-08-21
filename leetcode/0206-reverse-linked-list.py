# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            nxt = curr.next # store ref to rest of list
            curr.next = prev # reverse arrow dir
            prev = curr # move to front of list
            curr = nxt # move curr to next
        
        return prev
