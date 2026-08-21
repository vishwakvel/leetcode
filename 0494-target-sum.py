class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(index, total):
            if index == len(nums):
                return 1 if total == target else 0

            if (index, total) in memo:
                return memo[(index, total)]

            add = dp(index + 1, total + nums[index])
            subtract = dp(index + 1, total - nums[index])

            memo[(index, total)] = add + subtract
            return memo[(index, total)]

        return dp(0, 0)
