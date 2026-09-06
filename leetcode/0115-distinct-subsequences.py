class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1

        for char in s:
            for i in range(len(t) - 1, -1, -1):
                if char == t[i]:
                    dp[i + 1] += dp[i]
        
        return dp[-1]