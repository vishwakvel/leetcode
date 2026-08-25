import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for e1, e2, w in edges:
            graph[e1].append((e2, w))
            graph[e2].append((e1, 2*w))
        
        dist = {node: float("inf") for node in range(n)}
        dist[0] = 0

        heap = [(0, 0)] # cost, node

        while heap:
            cost, node = heapq.heappop(heap)

            if cost > dist[node]:
                continue
            
            if node == n-1:
                return cost
            
            for neighbor, weight in graph[node]:
                new = cost + weight

                if new < dist[neighbor]:
                    dist[neighbor] = new
                    heapq.heappush(heap, (new, neighbor))
        
        return -1