class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtracking(total, path, index):
            if total == target:
                ans.append(path.copy())
                return
            
            if total > target:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                if total + candidates[index] > target:
                    break

                path.append(candidates[i])
                backtracking(total+candidates[i], path, i+1)
                path.pop()
        
        backtracking(0, [], 0)
        return ans
