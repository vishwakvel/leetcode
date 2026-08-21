class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [] # stores indices
        ans = [0] * len(prices)

        for index, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                i = stack.pop()
                ans[i] = prices[i] - price
            
            stack.append(index)
        
        while stack:
            i = stack.pop()
            ans[i] = prices[i]
        
        return ans
