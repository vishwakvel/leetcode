class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)

        for prev, course in relations:
            graph[prev].append(course)
        
        memo = {}
        
        def dfs(course):
            if course in memo:
                return memo[course]
            
            longest = 0 

            for neighbor in graph[course]:
                longest = max(longest, dfs(neighbor)) # longest time path of all courses before the current course
            
            memo[course] = time[course-1] + longest # add curr course's time
            return memo[course]
        
        ans = 0

        for i in range(1, n+1):
            ans = max(ans, dfs(i))
        
        return ans
