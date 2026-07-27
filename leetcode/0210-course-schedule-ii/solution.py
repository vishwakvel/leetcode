class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        states = [0] * numCourses
        ans = []
        
        def dfs(course):
            if states[course] == 1:
                return False
            
            if states[course] == 2:
                return True
            
            states[course] = 1

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            states[course] = 2
            ans.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return ans[::-1]
