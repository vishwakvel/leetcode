class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)

        for num in reversed(nums):
            if total - num > num:
                return total
            
            total -= num
        
        return -1
