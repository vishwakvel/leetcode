class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dp(index):
            if index == len(nums)-1:
                return 0
            
            if index in memo:
                return memo[index]
            
            ans = float("inf")
            
            for i in range(1, nums[index]+1):
                if index + i < len(nums):
                    ans = min(ans, 1 + dp(index+i))
                
            memo[index] = ans
            return ans
        
        return dp(0)
