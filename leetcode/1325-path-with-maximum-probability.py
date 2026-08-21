import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))

        heap = [(-1, start_node)] # max heap
        probs = {}

        while heap:
            prob, node = heapq.heappop(heap)

            if node in probs:
                continue
            
            probs[node] = -prob

            for neighbor, weight in graph[node]:
                if neighbor not in probs:
                    heapq.heappush(heap, ((prob * weight), neighbor))
        
        if end_node not in probs:
            return 0
        
        return probs[end_node]
