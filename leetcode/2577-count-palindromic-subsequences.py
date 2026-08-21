class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        if n < 5:
            return 0
        
        rightpairs = [[0] * 10 for i in range(10)] # times each pair can occur
        rightcount = [0] * 10 # number of times digit appears to right

        for char in reversed(s):
            d = int(char)

            for i in range(10):
                rightpairs[d][i] += rightcount[i]
            
            rightcount[d] += 1
        
        left_pairs = [[0] * 10 for i in range(10)]
        left_count = [0] * 10

        ans = 0

        for char in s:
            mid = int(char)
            rightcount[mid] -= 1
            
            for j in range(10):
                rightpairs[mid][j] -= rightcount[j]
            
            for a in range(10):
                for b in range(10):
                    ans = (ans + left_pairs[a][b] * rightpairs[b][a]) % MOD
            
            for x in range(10):
                left_pairs[x][mid] += left_count[x]

            left_count[mid] += 1
    
        return ans
