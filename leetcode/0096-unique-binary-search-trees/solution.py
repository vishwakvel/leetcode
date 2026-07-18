class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1): # pick possible roots
                dp[i] += dp[j-1] * dp[i-j] # left * right subtrees
        
        return dp[-1]
