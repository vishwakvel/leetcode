from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        ans = 0
        left = 0

        for right in range(len(nums)):
            hmap[nums[right]] += 1

            while hmap[nums[right]] > k:
                hmap[nums[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
