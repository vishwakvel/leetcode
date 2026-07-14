class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = {}

        def dfs(day, holding):
            if day >= len(prices):
                return 0

            if (day, holding) in profit:
                return profit[(day, holding)]
            
            if holding:
                ans = max(dfs(day + 1, True), prices[day] + dfs(day + 2, False)) # max of keeping today or selling today
            else:
                ans = max(dfs(day + 1, False), -prices[day] + dfs(day + 1, True)) # max of skipping today or buying today
            
            profit[(day, holding)] = ans
            return ans
        
        return dfs(0, False)
