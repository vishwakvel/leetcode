class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = piles[-1]
        ans = right

        while left <= right:
            mid = (left + right) // 2

            hours = sum(ceil(x/mid) for x in piles)
            
            if hours <= h:
                ans = mid
                right = mid - 1
            elif hours > h:
                left = mid + 1
        
        return ans
