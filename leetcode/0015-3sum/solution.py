class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        1. Sort nums so that you can use two pointers method
        2. Approach this as doing a 2 sum for each num in nums list
        3. Go through each num in nums. For each:
            a) For any element at index greater than 0 if it's value is equal to the previous, then skip. This is because the previous num already has been accounted for so redoing the value will lead to the same answer.
            b) Set left as next element and right as the last element
            c) Now time for 2 sum but theres a change for if total is equal to 0
                a) When equal to 0, add the answer to the list. Then we move left and right closer to the center once. Now, we do the same thing as we did in step 3a which is to make sure we are using unique elements. We while loop through until we find a unique left and unique right and then continue the process. This is to make sure there's no duplicates.
        """
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        
        return ans
