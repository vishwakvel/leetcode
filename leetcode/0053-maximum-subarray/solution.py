class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = float("-inf")
        m = float("-inf")

        for num in nums:
            curr += num

            if num > curr:
                curr = num
            
            m = max(m, curr)
        
        return m
