class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def backtracking(path, index):
            ans.append(path.copy())

            for i in range(index, len(nums)):
                if i > index and nums[i-1] == nums[i]: # > index and not 0 because we need to compare with those on same level which means starting at index and not looking at ones chosen before
                    continue
                
                path.append(nums[i])
                backtracking(path, i+1)
                path.pop()
        
        backtracking([], 0)
        return ans
