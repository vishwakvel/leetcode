class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(path, index, target):
            if target == 0:
                ans.append(path.copy())
                return
            
            if target < 0:
                return
            
            for i in range(index, len(candidates)): # still a start index because once we move forward we dont want to go back since order doesn't matter
                path.append(candidates[i])
                backtrack(path, i, target-candidates[i]) # keep i so that you can reuse curr index (doesn't mean u can go backward)
                path.pop()
        
        backtrack([], 0, target)
        return ans
