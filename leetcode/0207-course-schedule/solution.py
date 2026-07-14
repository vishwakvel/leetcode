class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1: # cycle
                return False
            
            if state[course] == 2: # alr checked
                return True
            
            state[course] = 1

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            state[course] = 2 # finished
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
