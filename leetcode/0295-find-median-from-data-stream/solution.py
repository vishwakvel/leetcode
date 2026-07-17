import heapq

class MedianFinder:
    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        if not self.small or num < -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        if len(self.small) > len(self.large) + 1:
            n = -heapq.heappop(self.small)
            heapq.heappush(self.large, n)
        
        if len(self.large) > len(self.small):
            n = heapq.heappop(self.large)
            heapq.heappush(self.small, -n)


    def findMedian(self) -> float:
        if (len(self.small) + len(self.large)) % 2 == 1:
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
