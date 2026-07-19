import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        heap = []
        time = 0

        for duration, deadline in courses:
            time += duration
            heapq.heappush(heap, -duration)

            if time > deadline:
                longest = -heapq.heappop(heap)
                time -= longest
        
        return len(heap)
