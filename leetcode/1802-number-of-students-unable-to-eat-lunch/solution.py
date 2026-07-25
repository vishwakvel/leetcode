from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        i = 0
        rotations = 0

        while queue:
            if queue[0] == sandwiches[i]:
                queue.popleft()
                i += 1
                rotations = 0
            else:
                queue.append(queue.popleft())
                rotations += 1
            
            if rotations == len(queue):
                break
        
        return len(queue)
