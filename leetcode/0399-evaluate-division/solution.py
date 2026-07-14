class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for index, (var1, var2) in enumerate(equations):
            graph[var1].append((var2, values[index]))
            graph[var2].append((var1, 1/values[index]))
        
        def dfs(curr, target, visited):
            if curr == target:
                return 1.0
            
            visited.add(curr)

            for neighbor, weight in graph[curr]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)

                    if result != -1:
                        return weight * result
            
            return -1
        
        ans = []

        for start, end in queries:
            if start not in graph or end not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(start, end, set()))
        
        return ans
