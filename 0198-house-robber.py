class Solution:
    def rob(self, nums: List[int]) -> int:
        # 2 choices either rob td and skip tmrw or skip td and move onto tmrw
        memo = {}

        def dp(index):
            if index >= len(nums):
                return 0
            
            if index in memo:
                return memo[index]
            
            memo[index] = max(nums[index] + dp(index+2), dp(index+1))
            return memo[index]
        
        return dp(0)
