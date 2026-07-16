class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        money = {}

        def dp(house):
            if house >= len(nums):
                return 0
            
            if house in money:
                return money[house]

            money[house] = max(nums[house] + dp(house + 2), dp(house + 1))

            return money[house]
        
        return dp(0)
"""
        if len(nums) == 1:
            return nums[-1]
            
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[-1]
