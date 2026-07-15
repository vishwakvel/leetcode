class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(path):
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtracking(path)
                    path.pop()
        
        backtracking([])
        return ans
