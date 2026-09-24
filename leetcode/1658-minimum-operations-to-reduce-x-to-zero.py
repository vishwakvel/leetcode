class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x

        if target < 0:
            return -1
        
        if target == 0:
            return len(nums)

        left = 0
        longest = -1
        window = 0

        for right in range(len(nums)):
            window += nums[right]

            while window > target:
                window -= nums[left]
                left += 1
            
            if window == target:
                longest = max(longest, right - left + 1)
        
        if longest == -1:
            return -1
        
        return len(nums) - longest