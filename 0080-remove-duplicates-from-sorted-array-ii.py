class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        left = 0

        while left < len(nums):
            right = left

            while right < len(nums) and nums[right] == nums[left]:
                right += 1
        
            nums[write] = nums[left]
            write += 1
            count = right - left
            
            if count > 1:
                nums[write] = nums[left]
                write += 1
            
            left = right
        
        return write
