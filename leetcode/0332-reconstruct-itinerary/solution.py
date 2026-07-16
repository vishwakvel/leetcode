class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # eurlerian path - use all edges only once (edge is ticket)
        graph = defaultdict(list)
        ans = []

        for start, end in sorted(tickets, reverse=True):
            graph[start].append(end)
        
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            
            ans.append(airport)
        
        dfs("JFK")
        return ans[::-1]
