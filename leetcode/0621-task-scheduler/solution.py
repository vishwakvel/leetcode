class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        ready = [(-count, task) for task, count in freq.items()]
        heapq.heapify(ready)
        cooldown = []
        time = 0

        while ready or cooldown:
            while cooldown and cooldown[0][0] <= time:
                _, count, task = heapq.heappop(cooldown)
                heapq.heappush(ready, (count, task))
            
            if ready:
                count, task = heapq.heappop(ready)
                count += 1

                if count < 0:
                    heapq.heappush(cooldown, (time + n + 1, count, task))
            
            time += 1

        return time
