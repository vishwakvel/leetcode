class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i in range(len(equations)):
            start, end = equations[i]
            graph[start].append((end, values[i]))
            graph[end].append((start, 1/values[i]))
        
        def dfs(start, end, visited):
            if start == end:
                return 1.0
            
            visited.add(start)
            
            for neighbor, weight in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)

                    if result != -1:
                        return weight * result
            
            return -1
        
        ans = []

        for start, end in queries:
            if start not in graph or end not in graph:
                ans.append(-1)
            else:
                ans.append(dfs(start, end, set()))
        
        return ans
