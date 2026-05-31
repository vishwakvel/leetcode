class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Swap zeros first then ones
        """
        left = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1

        for i in range(left, len(nums)):
            if nums[i] == 1:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
