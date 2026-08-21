class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        
        ans = []
        maxes = deque() # indexes sorted by vals decreasing (greatest -> least)

        for right in range(len(nums)):
            if maxes and maxes[0] < right - k + 1:
                maxes.popleft()
            
            while maxes and nums[maxes[-1]] < nums[right]:
                maxes.pop()
            
            maxes.append(right)

            if right >= k - 1:
                ans.append(nums[maxes[0]])
        
        return ans
