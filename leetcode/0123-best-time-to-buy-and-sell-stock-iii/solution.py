class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = {}

        def dp(day, holding, count):
            if day == len(prices):
                return 0 if not holding else float("-inf")
            
            if count == 2:
                return 0
            
            if (day, holding, count) in profit:
                return profit[(day, holding, count)]
            
            if not holding:
                profit[(day, holding, count)] = max(-prices[day] + dp(day+1, True, count), dp(day+1, False, count))
            else: # sell td
                profit[(day, holding, count)] = max(prices[day] + dp(day+1, False, count+1), dp(day+1, True, count))
            
            return profit[(day, holding, count)]
        
        return dp(0, False, 0)
