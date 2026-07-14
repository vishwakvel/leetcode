class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = float("-inf")
        max_sum = float("-inf")

        for num in nums:
            curr_sum += num
            
            if num > curr_sum:
                curr_sum = num
            
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
