class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        visited = set()
        
        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            
            return False
        
        return dfs(source)
