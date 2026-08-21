class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return False
            
            if size[px] < size[py]:
                parent[px] = py
            elif size[px] > size[py]:
                parent[py] = px
            else:
                parent[py] = px
                size[px] += 1
            
            return True
        
        for i, j in edges:
            if not union(i, j):
                return [i, j]
