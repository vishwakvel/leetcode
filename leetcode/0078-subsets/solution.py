class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # every path is an answer
        ans = []

        def backtracking(path, start):
            ans.append(path.copy())

            for i in range(start, len(nums)): # since u can't reuse any numbers you start from left to right and every time u move up u have start so that u cant look backward
                path.append(nums[i])
                backtracking(path, i+1)
                path.pop()
        
        backtracking([], 0)
        return ans
