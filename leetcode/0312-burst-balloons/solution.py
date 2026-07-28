class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        memo = {}

        def dp(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            
            if left + 1 == right:
                return 0
            
            ans = 0
            
            for i in range(left + 1, right):
                coins = nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right)
                ans = max(ans, coins)
            
            memo[(left, right)] = ans
            return ans
        
        return dp(0, n-1)
