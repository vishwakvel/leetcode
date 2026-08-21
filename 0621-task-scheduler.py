import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ready = [-freq for freq in Counter(tasks).values()]
        heapq.heapify(ready)
        cooling = deque()
        time = 0

        while cooling or ready:
            time += 1
            
            if ready:
                freq = heapq.heappop(ready)
                freq += 1

                if freq != 0:
                    cooling.append((time+n, freq))

            if cooling and cooling[0][0] == time:
                _, freq = cooling.popleft()
                heapq.heappush(ready, freq)
        
        return time
