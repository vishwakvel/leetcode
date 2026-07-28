class Solution:
    def minMoves(self, nums: List[int]) -> int:
        largest = max(nums)
        ans = 0

        for num in nums:
            ans += largest - num
        
        return ans
