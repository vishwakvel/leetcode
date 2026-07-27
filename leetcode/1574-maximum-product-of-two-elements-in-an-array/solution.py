class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = second = 0

        for num in nums:
            if not first:
                first = num
            else:
                if num > first:
                    second = first
                    first = num
                else:
                    second = max(second, num)
        
        return (first-1)*(second-1)
