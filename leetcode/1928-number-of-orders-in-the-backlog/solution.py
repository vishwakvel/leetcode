import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10**9 + 7
        buy = [] # max heap
        sell = [] # min heap

        for order in orders:
            price, amount, orderType = order

            if orderType == 0: # buy order
                while amount > 0 and sell and sell[0][0] <= price:
                    sell_price, sell_amount = heapq.heappop(sell)
                    trade = min(amount, sell_amount)
                    amount -= trade
                    sell_amount -= trade

                    if sell_amount > 0:
                        heapq.heappush(sell, (sell_price, sell_amount))

                if amount > 0:
                    heapq.heappush(buy, (-price, amount))
            else:
                while amount > 0 and buy and -buy[0][0] >= price:
                    neg_buy_price, buy_amount = heapq.heappop(buy)
                    trade = min(amount, buy_amount)
                    amount -= trade
                    buy_amount -= trade

                    if buy_amount > 0:
                        heapq.heappush(buy, (neg_buy_price, buy_amount))

                if amount > 0:
                    heapq.heappush(sell, (price, amount))
        
        ans = 0

        while buy:
            ans = (ans + heapq.heappop(buy)[1]) % MOD
        
        while sell:
            ans = (ans + heapq.heappop(sell)[1]) % MOD

        return ans
