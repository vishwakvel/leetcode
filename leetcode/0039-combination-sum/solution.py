class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(start: int, path: List[int], remaining: int):
            if remaining == 0:
                ans.append(path[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remaining-candidates[i])
                path.pop()
        
        backtrack(0, [], target)
        return ans
