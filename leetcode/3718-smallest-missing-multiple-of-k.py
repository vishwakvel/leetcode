class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set()

        for num in nums:
            if num % k == 0:
                seen.add(num//k)
        
        counter = 1

        while counter in seen:
            counter += 1
        
        return counter * k