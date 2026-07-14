class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prevprev = 1
        prev = 2

        for i in range(3, n+1):
            curr = prev + prevprev
            prevprev = prev
            prev = curr
        
        return curr
