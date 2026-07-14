class Solution(object):
    def twoSum(self, nums, target):
        ans = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in ans:
                return [ans.get(diff), i]
            else:
                ans[nums[i]] = i
