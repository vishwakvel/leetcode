from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        time = 0

        for index, ticket in enumerate(tickets):
            queue.append((index, ticket))
        
        while queue:
            index, ticket = queue.popleft()
            time += 1
            
            if ticket == 1:
                if index == k:
                    return time
            else:
                queue.append((index, ticket-1))
