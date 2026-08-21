class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = {}

        def dp(day, holding):
            if day >= len(prices):
                return 0
            
            if (day, holding) in profit:
                return profit[(day, holding)]
            
            if holding:
                # hold or sell
                ans = max(dp(day+1, True), prices[day] + dp(day+1, False))
            else: # skip or buy
                ans = max(dp(day+1, False), -prices[day] + dp(day+1, True))
            
            profit[(day, holding)] = ans
            return ans
        
        return dp(0, False)
