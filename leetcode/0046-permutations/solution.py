class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(path): # no need for visited since theyre distinct ints
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtracking(path)
                    path.pop()
        
        backtracking([])
        return ans
