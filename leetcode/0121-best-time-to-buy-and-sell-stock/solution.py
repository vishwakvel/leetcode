class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        1. Sliding window, so we set buy as first element and sell as second.
        2. We check and see if sell is greater than buy
            a) If it is, then we calculate the profit and make sure to store the max of the current and previous in profit.
            b) If it isn't, then we move buy up to sell because why would we have that as our buy price when theres a smaller number after it
        3. We increment sell by 1
        """
        buy = 0
        sell = 1
        profit = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell

            sell += 1

        return profit
