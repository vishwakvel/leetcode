class Solution:
    def numDecodings(self, s: str) -> int:
        # each state is how many ways till index i
        memo = {}

        def dp(index):
            if index == len(s):
                return 1
            
            if s[index] == "0":
                return 0
            
            if index in memo:
                return memo[index]
            
            ways = dp(index + 1)
            
            if index + 1 < len(s) and 10 <= int(s[index:index + 2]) <= 26:
                ways += dp(index + 2)
            
            memo[index] = ways
            return ways

        return dp(0)
