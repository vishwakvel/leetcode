class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[n-1] - nums[0]

        for i in range(1, n):
            high = max(nums[i-1] + k, nums[n-1] - k) # smallest plus k vs largest - k
            low = min(nums[0] + k, nums[i] - k) # smallest plus k vs largest - k
            ans = min(ans, high - low)

        return ans
