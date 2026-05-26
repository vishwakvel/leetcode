class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        Strategy:
        1. Empty dictionary to store numbers as they are processed in for loop. Use dict because you want to also store the index and also because .get() is a O(1) process which makes it faster.
        2. Use a for loop to go through the nums list and for each num calculate the difference needed to satisfy the target.
        3. Check if the difference already exists in the ans dict
            a) If it does, then return the current num's index along with the index of the difference (which is stored in the ans dict as the value)
            b) If not, then add the num:index pair to the ans dict
        """
        ans = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in ans:
                return [ans.get(diff), index]
            else:
                ans[num] = index
