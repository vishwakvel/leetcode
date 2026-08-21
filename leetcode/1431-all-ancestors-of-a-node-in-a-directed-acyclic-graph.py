class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        for source, dest in edges:
            graph[source].append(dest)
        
        visited = [False] * n
        order = []

        def dfs(node):
            visited[node] = True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

            order.append(node)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)

        ancestors = [set() for i in range(n)]

        for node in reversed(order):
            for neighbor in graph[node]:
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)

        return [sorted(s) for s in ancestors]
