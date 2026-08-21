class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        ans = 0
        prev = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev:
                prev = end
            else:
                ans += 1
                prev = min(prev, end)
        
        return ans
