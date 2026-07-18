class Solution:
    def climbStairs(self, n: int) -> int:
        # state represents number of diff ways to climb i stairs
        if n <= 2:
            return n
            
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] += dp[i-1] + dp[i-2]
        
        return dp[-1]
