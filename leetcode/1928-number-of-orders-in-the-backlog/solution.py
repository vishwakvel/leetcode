import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10**9 + 7
        buyheap = [] # max heap -> price, amount
        sellheap = [] # min heap -> price, amount

        for price, amount, orderType in orders:
            if orderType == 0: # buy
                while sellheap and amount > 0 and sellheap[0][0] <= price:
                    sellprice, sellamount = heapq.heappop(sellheap)
                    trade = min(amount, sellamount)
                    amount -= trade
                    sellamount -= trade

                    if sellamount > 0:
                        heapq.heappush(sellheap, (sellprice, sellamount))
                
                if amount > 0:
                    heapq.heappush(buyheap, (-price, amount))
            else: # sell
                while buyheap and amount > 0 and -buyheap[0][0] >= price:
                    buyprice, buyamount = heapq.heappop(buyheap)
                    trade = min(amount, buyamount)
                    amount -= trade
                    buyamount -= trade

                    if buyamount > 0:
                        heapq.heappush(buyheap, (buyprice, buyamount))
                    
                if amount > 0:
                    heapq.heappush(sellheap, (price, amount))
        
        ans = 0

        for _, amount in buyheap:
            ans += amount
        
        for _, amount in sellheap:
            ans += amount
    
        return ans % MOD
