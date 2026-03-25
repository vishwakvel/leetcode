class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 2:
            return [0,1]
        
        ndict = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in ndict:
                return [ndict[diff], i]

            ndict[num] = i
