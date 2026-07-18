class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0] * (l2+1) for i in range(l1+1)]
        # state represents longest common subsequence till text1[:i] and text2[:j]

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1] # match so take diagonal
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # ignore one and take other
        
        return dp[-1][-1]
