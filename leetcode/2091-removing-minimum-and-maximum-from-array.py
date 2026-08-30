class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_index = 0
        max_index = 0

        for index, num in enumerate(nums):
            if num < nums[min_index]:
                min_index = index

            if num > nums[max_index]:
                max_index = index
            
        i = min(min_index, max_index)
        j = max(min_index, max_index)

        return min(j + 1, n - i, i + 1 + n - j) # both from front, both from back, one from front one from back