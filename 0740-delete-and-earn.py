from collections import Counter
import bisect

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        vals = sorted(count.keys())
        points = {}
        
        def dp(index):
            if index >= len(vals):
                return 0

            if index in points:
                return points[index]
            
            points[index] = max(dp(index+1), vals[index] * count[vals[index]] + dp(bisect.bisect_left(vals, vals[index] + 2)))

            return points[index]
        
        return dp(0)
