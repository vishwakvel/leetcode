class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # distinct odd factros - prime factorization
        while n % 2 == 0:
            n //= 2
        
        d = 3
        ans = 1

        while d * d <= n:
            count = 1

            while n % d == 0:
                n //= d
                count += 1
            
            ans *= count
            d += 2
        

        if n > 1:
            ans *= 2

        return ans
