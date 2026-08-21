class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7

        graph = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }

        dp = [1] * 10 # number where phone number ends at

        for i in range(n - 1):
            new = [0] * 10 # adding new number

            for digit in range(10):
                for nxt in graph[digit]:
                    new[nxt] += dp[digit] # for each val add (accumulates over vals not keys)
                    new[nxt] %= MOD
            
            dp = new
        
        return sum(dp) % MOD
