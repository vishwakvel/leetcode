class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = {}

        def dp(day, holding):
            if day >= len(prices):
                return 0

            if (day, holding) in profit:
                return profit[(day, holding)]
            
            if holding:
                profit[(day, holding)] = max(prices[day] + dp(day + 2, False), dp(day + 1, True))
            else:
                profit[(day, holding)] = max(-prices[day] + dp(day + 1, True), dp(day + 1, False))
            
            return profit[(day, holding)]

        return dp(0, False)
