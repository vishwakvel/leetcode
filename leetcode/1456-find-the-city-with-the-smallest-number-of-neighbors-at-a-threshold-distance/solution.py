class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float("inf")] * n for i in range(n)]

        for i in range(n):
            dist[i][i] = 0
        
        for f, t, w in edges:
            dist[f][t] = w
            dist[t][f] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        mincount = float("inf")
        ans = -1

        for i in range(n):
            count = 0

            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1
            
            if count <= mincount:
                mincount = count
                ans = i
        
        return ans
