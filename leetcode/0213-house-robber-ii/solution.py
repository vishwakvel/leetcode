class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            memo = {}

            def dp(i):
                if i >= len(arr):
                    return 0
                
                if i in memo:
                    return memo[i]

                memo[i] = max(arr[i] + dp(i + 2), dp(i + 1))
                return memo[i]

            return dp(0)

        if len(nums) == 1:
            return nums[0]

        return max(helper(nums[:-1]), helper(nums[1:])) # exlude last vs exclude first
