class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total = 0
        product = 1

        for char in str(n):
            total += int(char)
            product *= int(char)
        
        return n % (total + product) == 0