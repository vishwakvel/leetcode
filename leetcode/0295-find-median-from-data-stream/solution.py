import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if not self.large or num < self.large[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        if len(self.small) > len(self.large) + 1:
            popped = heapq.heappop(self.small)
            heapq.heappush(self.large, -popped)
        
        if len(self.large) > len(self.small):
            popped = heapq.heappop(self.large)
            heapq.heappush(self.small, -popped)

    def findMedian(self) -> float:
        if (len(self.small) + len(self.large)) % 2 == 1:
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
