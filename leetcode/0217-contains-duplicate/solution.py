class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        1. Convert nums list into set
        2. Check if the set and nums list have the different length
            a) If they do then true
            b) If they don't then false
        """
        nums_set = set(nums)
        return len(nums_set) != len(nums)
