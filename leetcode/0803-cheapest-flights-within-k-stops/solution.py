import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for source, dest, price in flights:
            graph[source].append((dest, price))
        
        heap = [(0, src, 0)] # cost is first element so sorted by cost

        dp = [[float("inf")] * (k+2) for i in range(n)] # min cost for each city and the flights already taken (k+2) because stops is 1 less than flights
        dp[src][0] = 0

        while heap:
            cost, city, count = heapq.heappop(heap)

            if city == dst:
                return cost
            
            if count == k + 1:
                continue
            
            for neighbor, price in graph[city]:
                newcost = cost + price

                if newcost < dp[neighbor][count+1]:
                    dp[neighbor][count+1] = newcost
                    heapq.heappush(heap, (newcost, neighbor, count+1))
        
        return -1
