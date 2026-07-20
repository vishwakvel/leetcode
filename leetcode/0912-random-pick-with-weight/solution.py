import bisect

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        curr = 0

        for weight in w:
            curr += weight
            self.prefix.append(curr)
        
        self.total = curr

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
