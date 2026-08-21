class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        if x <= 3:
            return 1
        
        left = 2
        right = x // 2

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid 
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
