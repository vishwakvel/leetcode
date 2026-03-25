class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums)) # set() of nums removes duplicates so if the length is different then there had to have been duplicates in nums
