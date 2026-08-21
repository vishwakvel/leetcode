class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        ans = []

        for i, num in enumerate(nums):
            if num > 0:
                ans.append(i + 1)
        
        return ans
