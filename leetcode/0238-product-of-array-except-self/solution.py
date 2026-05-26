class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1. Create ans list that is same length as nums list and default val is set to 1
        2. Go through left first, so multiply ans[i] with each element in nums that is to the left
            a) Have accumulator that you change everytime
            b) Update ans[i] first then change acc
        3. Go through right next, so multiply ans[i] with each element in nums that is to the right
            a) Have accumulator that you change everytime (multiply because you have to keep left's progress)
            b) update ans[i] first then change acc
        """
        nums_len = len(nums)
        ans = [1] * nums_len

        left = 1
        for i in range(nums_len):
            ans[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(nums_len - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        
        return ans
