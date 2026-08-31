# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        index = 1
        first = -1
        recent = -1
        minans = float("inf")

        while curr.next:
            nxt = curr.next

            if (curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val):
                if first == -1:
                    first = index
                else:
                    minans = min(minans, index - recent)

                recent = index

            prev = curr
            curr = curr.next
            index += 1

        if first == -1 or first == recent:
            return [-1, -1]

        maxans = recent - first
        return [minans, maxans]